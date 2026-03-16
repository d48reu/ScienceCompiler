Butyrate / Neuroinflammation Priority Review

You do NOT need to figure out the workflow yourself. I already ran it.

Start here, in this order:

1. Main story
   /home/d48reu/science-compiler/corpora/butyrate_neuroinflammation/reports/SUMMARY.md

2. The actual contradiction rows
   /home/d48reu/science-compiler/corpora/butyrate_neuroinflammation/review_queue/contradictions_review.csv

3. The main evidence bucket
   /home/d48reu/science-compiler/corpora/butyrate_neuroinflammation/review_queue/evidence_balance_review.csv
   Look specifically at the row:
   - intervention = sodium butyrate
   - outcome = neuroinflammation

4. Highest-priority claim rows
   /home/d48reu/science-compiler/corpora/butyrate_neuroinflammation/review_queue/claims_review.csv
   Focus on these claim_ids first:
   - pmid_32556930::C1   (negative Parkinson/MPTP result)
   - pmid_33785315::C1   (positive 5XFAD Alzheimer result)
   - pmid_36555338::C1   (positive binge-ethanol result)
   - pmid_36709599::C1   (positive chronic alcohol result)
   - pmid_38340407::C1   (positive lead neurotoxicity result)
   - pmid_39962509::C1   (positive cardiac-arrest result)

What I need you to sanity-check

A. Is each of those 6 claims actually fair?
   Meaning:
   - is the outcome label right?
   - is the effect sign right?
   - is the summary too strong or too weak?

B. Are the contradictions real enough?
   Most likely answer: yes, but context-conditioned.
   What I want to know is whether any contradiction is fake because of bad extraction.

C. Is "sodium butyrate -> neuroinflammation" a fair grouped bucket?
   If yes, keep it.
   If no, we may need to split by disease family.

My current best guess
- The contradiction cluster is real, not fake.
- The negative MPTP Parkinson paper is the main outlier against a broader positive set.
- Next likely improvement is bucket splitting by disease context, not deleting the contradiction.

If you want the absolute minimum to read:
- SUMMARY.md
- contradictions_review.csv
- the sodium butyrate/neuroinflammation row in evidence_balance_review.csv
