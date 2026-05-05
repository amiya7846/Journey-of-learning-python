# Journey-of-learning-python
In this repo I will learn all the fundamental concepts of python programming. I will cover all the topics chapter wise so it will be helpful for revision and also it will helpfull for others.
FILE: requirements.txt
Include: fastapi, uvicorn, python-multipart, anthropic, pymupdf, python-docx,
scikit-learn, numpy, reportlab, python-dotenv, aiofiles

FILE: main.py
FastAPI app with these exact endpoints:
- POST /upload-tender → accepts PDF/DOCX, returns extracted criteria JSON
- POST /upload-bid → accepts PDF/JPG/PNG, returns chunk count and preview
- POST /evaluate → runs full TF-IDF + Claude pipeline, returns all verdicts
- GET /audit-trail → returns complete audit log
- POST /override → officer overrides a verdict, logs to audit trail
- GET /report → generates and returns PDF evaluation report
- DELETE /reset → clears all session data
- GET /session-status → returns what has been uploaded
Enable CORS for all origins.
Store session data in memory dict (no database needed for prototype).

FILE: tender_parser.py
Function: parse_tender(file_path) → dict
- Auto-detect if PDF is scanned or text-based
- For text PDF: use PyMuPDF to extract text page by page
- For scanned PDF: use Claude Vision to OCR each page
- Send full tender text to Claude API with this instruction:
  "Extract ALL eligibility criteria and return as JSON array.
   Each criterion must have: id, name, type (financial/technical/
   certification/experience/other), description, threshold,
   threshold_unit, required_documents, is_mandatory"
- Parse Claude's JSON response
- Return dict with criteria list and total count

FILE: bid_extractor.py
Function: extract_bid(file_path) → dict
- Support file types: .pdf, .jpg, .jpeg, .png, .bmp, .tiff
- For text PDF: use PyMuPDF, extract page by page
- For scanned PDF: use Claude Vision OCR page by page at 300 DPI
- For image files: use Claude Vision to read the image
- Chunk the extracted text into 600-word overlapping windows
- Return: pages list, chunks list (with page number), full_text, counts

FILE: matching_engine.py
Function: match_criterion_to_bid(criterion, chunks) → dict
Step 1 — TF-IDF pre-filter:
- Build criterion_text from name + description + threshold_unit
- Use TfidfVectorizer(stop_words='english', ngram_range=(1,2))
- Fit on [criterion_text] + all chunk texts
- Compute cosine_similarity between criterion and all chunks
- Sort by similarity score, take top 5 chunks
- Log the top TF-IDF score

Step 2 — Claude evaluation:
- Send criterion details + top 5 chunks to Claude API
- Prompt Claude to return ONLY this JSON:
  {
    "verdict": "Eligible" | "Not Eligible" | "Needs Manual Review",
    "confidence": float 0.0 to 1.0,
    "evidence_quote": "exact quote from evidence",
    "page_reference": "Page X",
    "reasoning": "2-3 sentence explanation"
  }
- Never fabricate evidence. Only use what is in the chunks.

Step 3 — Confidence threshold:
- If confidence < 0.75, force verdict to "Needs Manual Review"
- Update reasoning to note it was auto-flagged

Step 4 — Log to audit trail via audit_logger.py

Function: evaluate_all_criteria(criteria, chunks) → list
- Loop through all criteria and call match_criterion_to_bid
- Return list of all verdict dicts

FILE: audit_logger.py
- Storage: local JSON file audit_trail.json
- Function log_verdict(): appends new entry with all fields including tfidf_score
- Function log_override(): appends override entry with original and new verdict
- Function get_full_audit(): returns all entries
- Function clear_audit(): clears the file
- Every entry must have: id, timestamp, criterion_id, criterion_name,
  verdict, confidence, tfidf_similarity_score, evidence_quote,
  page_reference, reasoning, overridden, override_note, officer_name

FILE: report_generator.py
- Use reportlab to generate a professional PDF report
- Include: CRPF header, tender name, bidder name, date
- Summary table: total / eligible / not eligible / needs review
- Detailed section for each criterion with verdict, confidence,
  TF-IDF score, evidence quote, page reference, reasoning
- Official footer with disclaimer

FILE: .env.example
ANTHROPIC_API_KEY=your_key_here

FILE: Procfile
web: uvicorn main:app --host 0.0.0.0 --port $PORT

FILE: railway.json
Standard Railway deploy config with uvicorn start command

FILE: runtime.txt
python-3.11
