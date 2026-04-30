# SKILL: DRAFTING A STATEMENT OF DEFENCE (LAGOS HIGH COURT)

This skill provides an automated workflow for drafting a **Statement of Defence** based on the *High Court of Lagos State (Civil Procedure) Rules 2019* and established pleading doctrines.

## I. INPUT REQUIREMENTS
1. **Statement of Claim (SoC):** The full text of the Claimant's allegations.
2. **Client's Narration:** The raw factual account, evidence, and documents provided by the Defendant.

## II. DRAFTING ALGORITHM (EXECUTION STEPS)

### Step 1: Pleading Delineation
*   **Filter for Materiality:** Extract only facts that establish a defense or support a denial.
*   **Remove Evidence:** Strip out exact transaction details, specific conversation quotes, and mentions of documents (these go in the Witness Statement).
*   **Test:** "Can this fact stand without proof details?" 
    *   If Yes → Plead it.
    *   If No → It is evidence; remove it.

### Step 2: Mapping & Traverse (The Seriatim Traverse)
Process each paragraph of the SoC against the Client's Narration:
*   **ADMIT:** If the fact is unquestionably true (e.g., identity of parties, existence of a contract).
*   **DENY:** If the fact is false or contested.
*   **NOT ADMIT:** If the fact is outside the Defendant's knowledge; "put the Claimant to the strictest proof."

### Step 3: Construction of Phrases
Apply the legal vocabulary rules:
*   **AVER:** Use for assertion of contested material facts (e.g., "The Defendant avers that the loan was repaid...").
*   **STATE:** Use for neutral or explanatory background (e.g., "The Defendant states that he is a businessman...").
*   **SPECIFIC TRAVERSE:** When denying, always provide the Defendant's version of the facts (Positive Defence).

### Step 4: Structuring the Facts (Granularity & Flow)
*   **One Fact Per Paragraph:** Break down the narrative. Do not clump distinct sequential events (e.g., an assault, followed by property damage, followed by a police arrest) into one paragraph. Each material fact must be its own independent numbered averment so the opposing party can individually admit or deny it.
*   **Affirmative Transitions:** When asserting your own case, smoothly transition from direct traverse ("In answer to paragraph X...") into independent affirmative statements ("The Defendant further avers...") to control pacing and create a positive defensive narrative.

## III. STRUCTURE & TEMPLATE

### 1. Header
Standard Court Heading, Suit No, and Parties.

### 2. Opening Clause (MANDATORY)
> “SAVE AND EXCEPT as is expressly admitted herein, the Defendants deny each and every allegation of fact contained in the Statement of Claim as if same were set out and traversed seriatim.”

### 3. Admission Clause
> “The Defendants admit paragraphs [X, Y, Z] of the Statement of Claim.”

### 4. Denial Clause
> “The Defendants deny paragraphs [A, B, C] of the Statement of Claim and put the Claimants to the strictest proof thereof.”

### 5. Responsive Paragraphs (The "Answer")
For every denied paragraph that requires a counter-fact:
> “In answer to paragraph [X] of the Statement of Claim, the Defendants aver that [Counter-Fact]...”

### 6. Special Defences & General Averments
Include sections for:
*   Lack of Capacity/Authority.
*   Misconduct of Claimant (e.g., fraud, misappropriation).
*   Representative Capacity challenges.

### 7. Concluding Clause (MANDATORY)
> “The Defendants state that the allegations contained in the Statement of Claim are false, distorted, and constitute a misrepresentation of the true state of affairs, and urge this Honourable Court to dismiss the Claimants’ claims as lacking in merit.”

## IV. CRITICAL CONSTRAINTS (FOR AI AGENT)
*   **STRICT FORMATTING:** You MUST strictly replicate the exact visual layout, spacing, indentation, and dotted lines of the heading, parties, and signature/address blocks provided in any exemplar templates. Do not deviate from the literal layout of the court heading, suit number, parties blocks, signature arrays, or service addresses (e.g., "FOR SERVICE ON").
*   Do NOT use argumentative language.
*   Do NOT include legal arguments or case law citations (these are for Address/Submissions).
*   Ensure every paragraph and sub-paragraph is numbered.
*   Verify that any allegation of **Fraud** or **Illegality** is specifically particularized.
