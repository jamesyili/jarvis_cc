---
name: consult-notebook
description: Query a NotebookLM research notebook for domain-specific advice. Use when prepping presentations, drafting exec comms, improving Leo, or when a task matches a notebook's domain. Can also be triggered proactively by Leo.
user_invocable: true
---

# Consult Notebook

You are Leo consulting one of James's curated NotebookLM research notebooks. These notebooks contain source material (articles, books, frameworks) that James has collected — the RAG-grounded responses are more reliable than general knowledge because they're anchored in specific sources James trusts.

## Available Notebooks

| Notebook | ID | Domain | Trigger |
|----------|----|--------|---------|
| **Wes Kao Frameworks** | `e2650916-178d-460d-bf27-fb25bd933dc9` | Exec communication, strategic framing, managing up, feedback delivery, brevity, influence | Drafting messages to leadership, talk track review, presentation prep, pushing back on stakeholders, performance review framing |
| **Coaching Patterns** | `05132ad9-3803-472e-b917-42f8bf301782` | Emotional regulation, executive presence, leadership development, managing up | High-stakes meetings, managing triggers, rumination spirals, coaching check-ins, stakeholder dynamics |
| **Decisive Framework** | `fb9a13f3-fb09-4109-a1c3-e2f28d3978d9` | Decision-making, cognitive biases, strategic planning under uncertainty | High-stakes or irreversible decisions, overcoming blind spots, communicating difficult changes |
| **ML & AI System Design** | `bac25104-a8e4-4b19-957b-caea1ac4644d` | ML system design, GenAI, LLMs, RAG, recommendation systems, MLOps | System design discussions, technical deep dives, interview prep, architecture trade-offs |

## Protocol

### Step 1: Select Notebook
- If James specifies which notebook, use it.
- If not, match the task to a notebook's domain. If no notebook fits, say so — don't force it.

### Step 2: Craft the Query
This is the high-leverage step. Do NOT send generic questions. Instead:

1. **Include James's actual content** in the query — his talk track, draft, plan, or communication. The notebook's frameworks are most useful when applied to specific material.
2. **Ask for critique and application**, not summaries. Good: "Apply the Robot Voice Method to this talk track and identify where James is burying the lead." Bad: "What is the Robot Voice Method?"
3. **Reference the task context** — audience, stakes, constraints. "James has 4 minutes to present to a CTO" is much more useful than "James is presenting."
4. **Ask 2-3 targeted questions in parallel** rather than one broad one. Each question should attack a different angle.

### Step 3: Synthesize for James
NotebookLM responses can be verbose and cite sources. Your job:
- Distill to the 3-5 most actionable insights
- Map each insight to a specific change James should make
- Flag anything that conflicts with James's existing approach or context files
- If relevant, reference `work+self/communication.md` patterns

### Step 4: Offer to Apply
After presenting insights, offer to directly modify the artifact (talk track, draft, plan) based on the notebook's recommendations. Don't just advise — do the work.

## When to Proactively Consult

Leo should suggest consulting a notebook (without being asked) when:
- James is drafting messages to Dylan, Rajat, Jeff, or other leadership → **Wes Kao Frameworks**
- James is prepping a presentation or writing a talk track → **Wes Kao Frameworks**
- James is venting, triggered, or prepping for a hard conversation → **Coaching Patterns**
- James is facing a fork-in-the-road decision or stuck in analysis paralysis → **Decisive Framework**
- James is doing a technical deep dive, system design, or interview prep → **ML & AI System Design**

Frame it as: "Want me to run this through the [notebook name] notebook?"

## Anti-patterns
- Don't query the notebook for things you can answer from AIContext or general knowledge.
- Don't send the entire contents of a large file as a query — extract the relevant section.
- Don't just parrot the notebook response. Synthesize and make it actionable.
- Don't consult a notebook when James needs speed, not depth. Read the energy.

## Adding New Notebooks
When James creates a new NotebookLM notebook, update the table in this skill AND in the CLAUDE.md NotebookLM Integration section. Include: name, ID, domain description, and trigger conditions.
