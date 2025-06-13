#!/usr/bin/env python3
"""
Ask Nick Chatbot Model
Creates a conversational AI model trained on Nicholas Konz's research, publications, and talks
"""

import torch
import torch.nn as nn
from transformers import (
    AutoTokenizer, 
    AutoModelForCausalLM, 
    TrainingArguments, 
    Trainer,
    DataCollatorForLanguageModeling,
    pipeline
)
from datasets import Dataset
import json
import os
import re
from typing import List, Dict, Any
import numpy as np
from datetime import datetime

class AskNickDataProcessor:
    """Processes research data into conversational training format"""
    
    def __init__(self):
        self.conversations = []
        self.context_data = {}
        
    def load_research_data(self):
        """Load all research-related data"""
        try:
            # Load scholar profile
            with open('../assets/json/scholar_profile.json', 'r') as f:
                self.context_data['profile'] = json.load(f)
            
            # Load publications from bibliography
            with open('../_bibliography/papers.bib', 'r') as f:
                self.context_data['bibtex'] = f.read()
                
            # Load CV data
            with open('../_data/cv.yml', 'r') as f:
                import yaml
                self.context_data['cv'] = yaml.safe_load(f)
                
        except Exception as e:
            print(f"Error loading research data: {e}")
            self.create_fallback_data()
    
    def create_fallback_data(self):
        """Create fallback data if files are not available"""
        self.context_data = {
            'profile': {
                'name': 'Nicholas Konz',
                'affiliation': 'Duke University',
                'interests': ['Machine Learning', 'Medical Imaging', 'Computer Vision', 'Deep Learning'],
                'publications': [
                    {
                        'title': 'Intrinsic Dataset Properties and Generalization in Neural Networks',
                        'year': 2024,
                        'venue': 'ICLR'
                    }
                ]
            }
        }
    
    def generate_training_conversations(self):
        """Generate realistic Q&A conversations about Nick's research"""
        
        # Research background questions
        self.add_conversation_set([
            ("Who is Nicholas Konz?", 
             "I'm Nicholas Konz, a Ph.D. candidate studying machine learning at Duke University under Maciej Mazurowski. My research focuses on deep learning for medical image analysis, spanning from application-oriented to foundational work."),
            
            ("What is your research focus?", 
             "My research centers on deep learning for medical image analysis, with emphasis on generative models, domain adaptation, and image-to-image translation. I'm particularly interested in foundational concepts like generalization and intrinsic geometric properties of datasets in medical imaging contexts."),
            
            ("Tell me about your background", 
             "I have an interdisciplinary background starting with physics and mathematics at UNC, where I worked on statistical techniques for astronomy. I then transitioned to machine learning and medical imaging at Duke, and have also interned at Pacific Northwest National Laboratory in their Math, Stats, and Data Science Group."),
             
            ("What makes your research unique?", 
             "My work bridges foundational deep learning concepts with practical medical imaging applications. I approach ML through a scientific lens, exploring how fundamental concepts like generalization theory and geometric properties of datasets apply to secondary domains like medical imaging."),
        ])
        
        # Technical research questions
        self.add_conversation_set([
            ("What are intrinsic dataset properties?", 
             "Intrinsic dataset properties refer to the fundamental geometric and statistical characteristics of datasets that influence how neural networks generalize. In my ICLR 2024 paper, I explore how these properties affect generalization in real-world applications, particularly in medical imaging."),
            
            ("How do you approach domain adaptation?", 
             "Domain adaptation is crucial in medical imaging where models need to work across different hospitals, scanners, or imaging protocols. I focus on techniques that bridge these domain gaps while maintaining diagnostic accuracy and reducing the need for extensive re-annotation."),
            
            ("What role do generative models play in your work?", 
             "Generative models are powerful tools for medical image synthesis, data augmentation, and understanding image distributions. I use them for tasks like creating synthetic medical data, improving model robustness, and developing better distance metrics between image distributions."),
             
            ("Tell me about your segmentation research", 
             "Medical image segmentation is about precisely identifying anatomical structures or pathologies in medical images. I work on advanced architectures, including diffusion-based approaches, to improve accuracy and reliability across different medical imaging modalities."),
        ])
        
        # Career and experience questions  
        self.add_conversation_set([
            ("What was your experience at PNNL?", 
             "At Pacific Northwest National Laboratory, I worked in the Math, Stats, and Data Science Group, which gave me valuable experience applying statistical methods to scientific problems and exposed me to the intersection of ML and scientific research."),
            
            ("How did you transition from physics to ML?", 
             "My physics and mathematics background provided a strong analytical foundation that naturally translated to machine learning. The statistical techniques I used in astronomy research were excellent preparation for understanding data distributions and model behavior in ML."),
            
            ("What teaching experience do you have?", 
             "I've been involved in teaching and mentoring throughout my PhD. I particularly enjoy helping students understand the mathematical foundations behind ML algorithms and their practical applications in scientific domains."),
             
            ("Tell me about your outreach work", 
             "I'm involved in the ERIRA program, which combines research mentoring with radio astronomy outreach. I also write tutorials and educational content, including featured articles on Towards Data Science, to make complex ML concepts more accessible."),
        ])
        
        # Future directions and philosophy
        self.add_conversation_set([
            ("What are your future research directions?", 
             "I'm excited about continuing to bridge foundational ML research with practical applications, particularly in scientific domains. I want to further explore how geometric and statistical properties of data can inform better model design and evaluation."),
            
            ("How do you view the future of ML in medicine?", 
             "ML in medicine has tremendous potential, but we need to focus on reliability, interpretability, and understanding failure modes. My work on intrinsic dataset properties aims to provide better foundations for understanding when and why models succeed or fail."),
            
            ("What advice would you give to students?", 
             "Develop strong mathematical foundations, be curious about interdisciplinary connections, and don't be afraid to bridge different fields. Some of the most interesting research happens at the intersections of disciplines."),
             
            ("What drives your research?", 
             "I'm motivated by the potential to improve healthcare through better AI tools, and by the intellectual challenge of understanding how learning algorithms really work. I believe in approaching ML scientifically, with rigorous analysis of fundamental principles."),
        ])
        
        return self.conversations
    
    def add_conversation_set(self, qa_pairs: List[tuple]):
        """Add a set of Q&A pairs to the training data"""
        for question, answer in qa_pairs:
            self.conversations.append({
                'input': question,
                'output': answer,
                'context': 'research_chat'
            })
    
    def format_for_training(self):
        """Format conversations for language model training"""
        formatted_data = []
        
        for conv in self.conversations:
            # Create a conversational format
            text = f"Human: {conv['input']}\n\nNick: {conv['output']}\n\n"
            formatted_data.append({'text': text})
            
            # Add variations with different question phrasings
            variations = self.generate_question_variations(conv['input'])
            for variation in variations:
                text = f"Human: {variation}\n\nNick: {conv['output']}\n\n"
                formatted_data.append({'text': text})
        
        return formatted_data
    
    def generate_question_variations(self, question: str) -> List[str]:
        """Generate variations of questions to improve model robustness"""
        variations = []
        
        # Simple variations
        if question.startswith("What"):
            variations.append(question.replace("What", "Can you tell me what"))
            variations.append(question.replace("What", "I'd like to know what"))
        
        if question.startswith("How"):
            variations.append(question.replace("How", "Can you explain how"))
            variations.append(question.replace("How", "I'm curious about how"))
        
        if question.startswith("Tell me"):
            variations.append(question.replace("Tell me about", "What can you tell me about"))
            variations.append(question.replace("Tell me about", "I want to learn about"))
        
        return variations[:2]  # Limit to 2 variations per question

class AskNickChatbot:
    """Main chatbot class using fine-tuned language model"""
    
    def __init__(self, model_name="microsoft/DialoGPT-small"):
        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        
    def prepare_data(self):
        """Prepare training data"""
        processor = AskNickDataProcessor()
        processor.load_research_data()
        conversations = processor.generate_training_conversations()
        formatted_data = processor.format_for_training()
        
        return Dataset.from_list(formatted_data)
    
    def load_base_model(self):
        """Load the base conversational model"""
        print(f"Loading base model: {self.model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
        
        # Add padding token if it doesn't exist
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
            
        self.model.to(self.device)
    
    def train_model(self, dataset, output_dir="./nick_chatbot_model"):
        """Fine-tune the model on research conversations"""
        if not self.model or not self.tokenizer:
            self.load_base_model()
        
        # Tokenize the dataset
        def tokenize_function(examples):
            return self.tokenizer(
                examples['text'], 
                truncation=True, 
                padding=True, 
                max_length=512
            )
        
        tokenized_dataset = dataset.map(tokenize_function, batched=True)
        
        # Data collator
        data_collator = DataCollatorForLanguageModeling(
            tokenizer=self.tokenizer,
            mlm=False,
        )
        
        # Training arguments
        training_args = TrainingArguments(
            output_dir=output_dir,
            overwrite_output_dir=True,
            num_train_epochs=3,
            per_device_train_batch_size=4,
            save_steps=100,
            save_total_limit=2,
            prediction_loss_only=True,
            logging_steps=50,
            warmup_steps=100,
            learning_rate=5e-5,
        )
        
        # Trainer
        trainer = Trainer(
            model=self.model,
            args=training_args,
            data_collator=data_collator,
            train_dataset=tokenized_dataset,
        )
        
        # Train the model
        print("Starting training...")
        trainer.train()
        
        # Save the model
        trainer.save_model()
        self.tokenizer.save_pretrained(output_dir)
        
        print(f"Model saved to {output_dir}")
    
    def load_trained_model(self, model_path="./nick_chatbot_model"):
        """Load the fine-tuned model"""
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_path)
            self.model = AutoModelForCausalLM.from_pretrained(model_path)
            self.model.to(self.device)
            print(f"Loaded trained model from {model_path}")
        except Exception as e:
            print(f"Could not load trained model: {e}")
            print("Loading base model instead...")
            self.load_base_model()
    
    def generate_response(self, question: str, max_length: int = 200) -> str:
        """Generate a response to a question"""
        # Format input
        input_text = f"Human: {question}\n\nNick:"
        
        # Tokenize
        inputs = self.tokenizer.encode(input_text, return_tensors="pt").to(self.device)
        
        # Generate response
        with torch.no_grad():
            outputs = self.model.generate(
                inputs,
                max_length=max_length,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id,
                eos_token_id=self.tokenizer.eos_token_id
            )
        
        # Decode response
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract just the response part
        if "Nick:" in response:
            response = response.split("Nick:")[-1].strip()
            # Clean up the response
            response = response.split("Human:")[0].strip()
        
        return response if response else "I'd be happy to discuss my research with you! Could you ask a more specific question?"
    
    def create_web_interface_code(self):
        """Generate JavaScript code for web integration"""
        js_code = '''
// Ask Nick Chatbot Web Interface
class AskNickChatbot {
    constructor() {
        this.apiEndpoint = '/api/chat';  // You'll need to set up this endpoint
        this.isLoading = false;
        this.conversationHistory = [];
        
        this.init();
    }
    
    init() {
        this.createChatInterface();
        this.setupEventListeners();
    }
    
    createChatInterface() {
        const chatContainer = document.createElement('div');
        chatContainer.id = 'nick-chatbot';
        chatContainer.innerHTML = `
            <div class="chatbot-header">
                <h3>💬 Ask Nick</h3>
                <p>Chat with me about my research and experience!</p>
            </div>
            <div class="chat-messages" id="chat-messages">
                <div class="bot-message">
                    Hi! I'm Nick. Feel free to ask me about my research in machine learning, 
                    medical imaging, or my journey from physics to AI. What would you like to know?
                </div>
            </div>
            <div class="chat-input-container">
                <input type="text" id="chat-input" placeholder="Ask me about my research..." />
                <button id="send-btn">Send</button>
            </div>
        `;
        
        return chatContainer;
    }
    
    setupEventListeners() {
        const input = document.getElementById('chat-input');
        const sendBtn = document.getElementById('send-btn');
        
        sendBtn.addEventListener('click', () => this.sendMessage());
        input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.sendMessage();
        });
    }
    
    async sendMessage() {
        const input = document.getElementById('chat-input');
        const message = input.value.trim();
        
        if (!message || this.isLoading) return;
        
        this.addMessage(message, 'user');
        input.value = '';
        this.isLoading = true;
        
        this.addTypingIndicator();
        
        try {
            const response = await this.getResponse(message);
            this.removeTypingIndicator();
            this.addMessage(response, 'bot');
        } catch (error) {
            this.removeTypingIndicator();
            this.addMessage('Sorry, I had trouble processing that. Could you try asking again?', 'bot');
        }
        
        this.isLoading = false;
    }
    
    async getResponse(message) {
        // In a real implementation, this would call your backend API
        // For now, we'll simulate with some basic responses
        return this.getSimulatedResponse(message);
    }
    
    getSimulatedResponse(message) {
        const lowerMessage = message.toLowerCase();
        
        if (lowerMessage.includes('research') || lowerMessage.includes('work')) {
            return "My research focuses on deep learning for medical image analysis. I work on generative models, domain adaptation, and understanding intrinsic dataset properties that affect generalization.";
        }
        
        if (lowerMessage.includes('background') || lowerMessage.includes('about')) {
            return "I'm a PhD candidate at Duke University working under Maciej Mazurowski. I have a background in physics and mathematics from UNC, and I'm passionate about applying ML to healthcare and scientific problems.";
        }
        
        if (lowerMessage.includes('medical imaging')) {
            return "Medical imaging is fascinating because it combines complex technical challenges with direct healthcare impact. I work on segmentation, generative models, and domain adaptation to make AI tools more reliable for medical applications.";
        }
        
        if (lowerMessage.includes('advice') || lowerMessage.includes('student')) {
            return "My advice for students is to build strong mathematical foundations, stay curious about interdisciplinary connections, and don't hesitate to bridge different fields. The most interesting research often happens at intersections!";
        }
        
        return "That's an interesting question! I'd love to discuss my research in machine learning and medical imaging. Could you be more specific about what aspect you'd like to know about?";
    }
    
    addMessage(text, sender) {
        const messagesContainer = document.getElementById('chat-messages');
        const messageDiv = document.createElement('div');
        messageDiv.className = `${sender}-message`;
        messageDiv.textContent = text;
        
        messagesContainer.appendChild(messageDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
    
    addTypingIndicator() {
        const messagesContainer = document.getElementById('chat-messages');
        const typingDiv = document.createElement('div');
        typingDiv.className = 'bot-message typing-indicator';
        typingDiv.id = 'typing-indicator';
        typingDiv.innerHTML = 'Nick is typing<span class="dots">...</span>';
        
        messagesContainer.appendChild(typingDiv);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
    
    removeTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
}

// Initialize chatbot when page loads
document.addEventListener('DOMContentLoaded', function() {
    const chatbot = new AskNickChatbot();
    // Add chatbot to page (you can customize placement)
    document.body.appendChild(chatbot.createChatInterface());
});
'''
        return js_code

def main():
    """Main training and setup function"""
    print("Setting up Ask Nick Chatbot...")
    
    # Create output directory
    os.makedirs("../assets/chatbot", exist_ok=True)
    
    # Initialize chatbot
    chatbot = AskNickChatbot()
    
    # Prepare training data
    print("Preparing training data...")
    dataset = chatbot.prepare_data()
    
    # Train the model
    print("Training chatbot model...")
    chatbot.train_model(dataset, output_dir="../assets/chatbot/nick_model")
    
    # Generate web interface code
    print("Generating web interface...")
    js_code = chatbot.create_web_interface_code()
    
    with open("../assets/js/ask_nick_chatbot.js", "w") as f:
        f.write(js_code)
    
    print("Ask Nick Chatbot setup complete!")
    print("Model saved to: ../assets/chatbot/nick_model")
    print("Web interface code saved to: ../assets/js/ask_nick_chatbot.js")
    
    # Test the model
    print("\nTesting the chatbot...")
    chatbot.load_trained_model("../assets/chatbot/nick_model")
    
    test_questions = [
        "What is your research about?",
        "Tell me about your background",
        "What advice would you give to students?",
        "How did you transition from physics to ML?"
    ]
    
    for question in test_questions:
        response = chatbot.generate_response(question)
        print(f"\nQ: {question}")
        print(f"A: {response}")

if __name__ == "__main__":
    main()