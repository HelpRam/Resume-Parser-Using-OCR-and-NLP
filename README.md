# Resume-Parser-Using-OCR-and-NLP



# Resume Parser: Extract and Analyze Key Information from Resumes

This project is a **Resume Parser** application that extracts and categorizes key information from resumes using **OCR (Optical Character Recognition)**, **Natural Language Processing (NLP)**, and **Machine Learning (ML)** techniques. The system processes resumes in PDF format to extract entities like names, organizations, locations, and dates, and analyzes this information to provide a structured summary.

---

## Features

- **PDF Resume Upload**: Allows users to upload resumes in PDF format for processing.
- **OCR-Based Text Extraction**: Utilizes Tesseract OCR to handle scanned resumes or image-based PDFs.
- **Named Entity Recognition (NER)**: Leverages SpaCy to identify entities like names, organizations, locations, and dates.
- **Machine Learning for Categorization**: Uses classification models to predict additional categories such as skills and education.
- **Preprocessing for Better Accuracy**: Includes robust preprocessing for text cleanup.
- **Downloadable Results**: Extracted information can be downloaded as a `.txt` file.
- **Streamlit UI**: A user-friendly and visually appealing interface with enhanced interactivity.

---

## Datasets Used

The project uses the **Kaggle Resume Dataset** as the primary source for training and testing. This dataset contains:
- Resumes in text and PDF formats.
- Labels for structured information such as skills, education, and work experience.

### Dataset Preprocessing
The raw dataset was preprocessed using the following steps:
1. **Text Cleaning**:
   - Removed non-ASCII characters and special symbols.
   - Tokenized text into sentences and words.
2. **Stopword Removal**:
   - Removed common stopwords like "and," "the," etc., using SpaCy's stopword list.
3. **Lemmatization**:
   - Applied lemmatization to normalize words (e.g., "running" → "run").
4. **NER Label Mapping**:
   - Mapped dataset labels to SpaCy's NER format for compatibility.
5. **OCR Integration**:
   - Converted PDF resumes to text and images, simulating real-world use cases.

---

## Machine Learning Techniques

1. **OCR**:
   - Used **Tesseract OCR** for extracting text from scanned or image-based resumes.
   - Integrated **pdf2image** for converting PDF pages to images.

2. **Named Entity Recognition (NER)**:
   - Fine-tuned **SpaCy's pre-trained `en_core_web_sm` model** on the Kaggle dataset.
   - Added custom entity categories for resumes:
     - Skills
     - Certifications
     - Experience
   - Achieved **F1-score of 88%** for custom NER tasks after fine-tuning.

3. **Classification**:
   - Trained a Logistic Regression model, random forest and XGbOOST model to classify extracted sentences into predefined categories (skills, education, work experience).
   - Achieved an **accuracy of 70%** on test data.

---

## Setup

### Requirements

Install the required dependencies using the following:

```bash
pip install -r requirements.txt
```

Ensure **Tesseract OCR** is installed and configured on your system.

### Download Pretrained SpaCy Model

Download the SpaCy language model:

```bash
python -m spacy download en_core_web_sm
```

---

## How to Run

1. **Launch the Application**:
   Run the following command to start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. **Upload Resume**:
   - Upload a PDF resume using the "Upload Resume" button.
   - Wait for the application to process the file.

3. **View Results**:
   - See extracted text and categorized entities displayed in a visually enhanced format.
   - Download the extracted text as a `.txt` file.

---

## Performance Metrics

| **Task**               | **Metric**  | **Score**  |
|-------------------------|-------------|------------|
| OCR Accuracy           | Character Recognition Accuracy | 96.5%     |
| NER (Custom Entities)  | F1-Score    | 88%        |
| Classification Accuracy | Accuracy    | 70%        |

---

## Highlights of the Streamlit UI

- **Modern Design**:
  - Custom icons and vibrant color schemes for categorized data.
  - Interactive upload button and progress bar.

- **Entity Highlighting**:
  - Names, organizations, locations, and dates are color-coded:
    - **Names**: Blue
    - **Organizations**: Green
    - **Locations**: Orange
    - **Dates**: Red

- **Download Option**:
  - Extracted text and entities can be downloaded for offline review.

---

## Future Enhancements

- **Deep Learning Models**:
  - Explore BERT-based models for improved NER and classification.
- **Resume Matching**:
  - Add functionality to match resumes with job descriptions.
- **Language Support**:
  - Extend support for multilingual resumes.
- **Web-Based Submission**:
  - Allow for API-based resume submissions for real-time parsing.

---

## License

This project is open-source and available under the **MIT License**.

---

=======
# Resume-Parser-Using-OCR-and-NLP
>>>>>>> 2e19fdf3dcab12786354323f932a621ed0029549
