# Granite 4.0 & 4.1 SLM Enterprise Use Case Matrix

*Julian Gonzalez, 2026*

## Purpose

This document maps selected IBM Granite 4.0 & 4.1 small language models (350M-3B) to practical enterprise use cases. It is designed for solution architects, AI engineers, platform teams, and enterprise automation teams evaluating compact models for retrieval, classification, extraction, workflow automation, and agentic AI systems.

## Scope

This matrix covers the Granite models listed in the source document.

| Model | Hugging Face model card |
|---|---|
| `ibm-granite/granite-4.0-h-350m` | <https://huggingface.co/ibm-granite/granite-4.0-h-350m> |
| `ibm-granite/granite-4.0-h-1b` | <https://huggingface.co/ibm-granite/granite-4.0-h-1b> |
| `ibm-granite/granite-4.0-h-micro` | <https://huggingface.co/ibm-granite/granite-4.0-h-micro> |
| `ibm-granite/granite-4.1-3b` | <https://huggingface.co/ibm-granite/granite-4.1-3b> |

## Validation Basis

This revision treats the IBM and Hugging Face model cards as authoritative sources for model identity, intended use, supported languages, context length, listed capabilities, tool-calling examples, and model limitations. The use-case recommendations below are expert guidance derived from those sources and should not be treated as benchmark results unless validated with task-specific evaluation data.

## Recommendation Levels

| Level | Meaning |
|---|---|
| **Primary fit** | Strong first candidate for this workload, subject to task-specific evaluation |
| **Secondary fit** | Useful in supporting roles or constrained deployment scenarios |
| **Use with evaluation** | Possible based on listed capabilities, but requires benchmark testing before production use |
| **Avoid as sole model** | Not recommended as the only model for the workflow |

> [!IMPORTANT]
> Model-card capabilities should be treated as evaluation starting points, not production guarantees. Validate each workflow with enterprise-specific data, tool schemas, safety tests, and escalation paths.

## Model Positioning Summary

| Model | Model class | Listed context length | Best enterprise role | Recommended deployment pattern |
|---|---:|---:|---|---|
| `granite-4.0-h-350m` | Lightweight instruct | 32K | High-volume utility model | Edge, on-device, batch classification, routing, simple extraction |
| `granite-4.0-h-1b` | Lightweight instruct, 1B family label | 128K | Lightweight enterprise workhorse | Domain-tuned assistant, short summarization, structured extraction, simple RAG |
| `granite-4.0-h-micro` | 3B long-context instruct | 128K | Granite 4.0 enterprise assistant | RAG, document QA, tool-enabled business assistant, code assistance |
| `granite-4.1-3b` | 3B long-context instruct | 131,072 | Primary agentic AI candidate | Tool-using agents, enterprise RAG, workflow automation, policy assistants |

## Use Case Fit Matrix

> [!NOTE]
> The fit ratings below are model-selection recommendations derived from published model-card capabilities, model size, context length, and intended-use statements. They are not benchmark results. Validate each rating with task-specific evaluation data before adopting it as an enterprise standard.

| Enterprise use case | `350m` | `1b` | `4.0-h-micro` | `4.1-3b` | Recommended default |
|---|---|---|---|---|---|
| Intent classification | Primary fit | Primary fit | Secondary fit | Secondary fit | `granite-4.0-h-350m` |
| Ticket routing | Primary fit | Primary fit | Secondary fit | Secondary fit | `granite-4.0-h-350m` |
| Email triage | Primary fit | Primary fit | Secondary fit | Secondary fit | `granite-4.0-h-350m` or `granite-4.0-h-1b` |
| Simple field extraction | Primary fit | Primary fit | Secondary fit | Secondary fit | `granite-4.0-h-1b` |
| Complex document extraction | Use with evaluation | Primary fit | Primary fit | Primary fit | `granite-4.0-h-1b` or `granite-4.1-3b` |
| Short summarization | Secondary fit | Primary fit | Primary fit | Primary fit | `granite-4.0-h-1b` |
| Long-context summarization | Avoid as sole model | Secondary fit | Primary fit | Primary fit | `granite-4.1-3b` |
| Retrieval augmented generation | Use with evaluation | Secondary fit | Primary fit | Primary fit | `granite-4.1-3b` |
| Knowledge base assistant | Use with evaluation | Secondary fit | Primary fit | Primary fit | `granite-4.1-3b` |
| Customer support copilot | Secondary fit for triage | Secondary fit | Primary fit | Primary fit | `granite-4.1-3b` |
| IT helpdesk assistant | Secondary fit for routing | Secondary fit | Primary fit | Primary fit | `granite-4.1-3b` |
| HR or policy assistant | Use with evaluation | Secondary fit | Primary fit | Primary fit | `granite-4.1-3b` |
| Function calling | Use with evaluation | Use with evaluation | Primary fit | Primary fit | `granite-4.1-3b` |
| API orchestration | Avoid as sole model | Use with evaluation | Secondary fit | Primary fit | `granite-4.1-3b` |
| Code completion | Secondary fit | Secondary fit | Primary fit | Primary fit | `granite-4.0-h-micro` or `granite-4.1-3b` |
| Code explanation | Use with evaluation | Secondary fit | Primary fit | Primary fit | `granite-4.1-3b` |
| Software engineering assistance with tool and human review | Avoid as sole model | Use with evaluation | Secondary fit | Primary fit | `granite-4.1-3b` |
| Multilingual dialog | Use with evaluation | Use with evaluation | Primary fit | Primary fit | `granite-4.1-3b` |
| Edge or on-device workflows | Primary fit | Secondary fit | Use with optimization | Use with optimization | `granite-4.0-h-350m` |
| High-volume batch processing | Primary fit | Primary fit | Secondary fit | Secondary fit | `granite-4.0-h-350m` |
| Safety or policy pre-screening | Secondary fit | Primary fit | Secondary fit | Secondary fit | Rules plus `granite-4.0-h-1b` |

> [!CAUTION]
> Multilingual support should be evaluated per language and task. Published language support does not guarantee equivalent quality across English and non-English workflows.

---

## Model-Specific Guidance

## `granite-4.0-h-350m`

### Best Fit

`granite-4.0-h-350m` is best suited for high-volume, low-latency utility tasks where the workflow is narrow, repeatable, and easy to evaluate.

### Clear Enterprise Use Cases

| Use case | Description | Example |
|---|---|---|
| Intent classification | Classify user requests into workflow categories | Route a message to HR, IT, finance, procurement, or legal |
| Ticket routing | Assign service requests to the correct queue | Route VPN, laptop, payroll, or benefits requests |
| Email triage | Label inbound messages by topic or urgency | Tag vendor emails as invoice, renewal, support, or sales |
| Simple field extraction | Extract known fields from short text | Pull invoice number, vendor, amount, due date, and PO number |
| Batch tagging | Apply labels to large volumes of records | Tag historical call-center notes or support tickets |
| RAG pre-filtering | Filter candidate chunks before a larger model answers | Remove irrelevant policy snippets before answer generation |
| Guardrail pre-screening | Flag requests that need policy review | Detect finance, HR, legal, or sensitive-data topics |
| Edge assistant | Run simple local assistance workflows | Field-service troubleshooting on constrained devices |

### Recommended Role

Use this model as a:

- Router
- Classifier
- Extractor
- Validator
- Pre-filter
- Edge utility model

### Avoid as Sole Model For

- Long-context reasoning
- Policy interpretation
- Multi-step tool use
- Complex code reasoning
- Autonomous agent planning
- High-risk decisions

### Production Notes

- Use deterministic schemas where possible.
- Evaluate per label, field, and routing class.
- Keep human escalation for sensitive topics.
- Use confidence thresholds and fallback logic.

---

## `granite-4.0-h-1b`

### Best Fit

`granite-4.0-h-1b` is a lightweight enterprise workhorse for workflows that need more capacity than 350M while still requiring efficient inference and practical domain adaptation.

### Clear Enterprise Use Cases

| Use case | Description | Example |
|---|---|---|
| Structured extraction | Extract fields from semi-structured documents | Parse procurement requests, renewals, invoices, and service forms |
| Short summarization | Summarize compact business records | Summarize a support thread before handoff |
| Ticket enrichment | Add metadata to incoming requests | Generate priority, product area, owner, and next action |
| Lightweight FAQ assistant | Answer common internal questions | Answer HR, facilities, travel, or procurement FAQs |
| Simple RAG | Answer questions over a constrained knowledge base | Retrieve and answer from a short policy library |
| Domain-specific fine-tuning | Adapt to enterprise-specific labels and formats | Classify insurance claims, incidents, or compliance requests |
| Response drafting | Draft short replies for human review | Draft an IT or HR support response |
| Tool selection | Choose from a small tool set | Select `lookup_user`, `create_ticket`, or `search_policy` |
| Multilingual triage | Classify or summarize multilingual messages | Route Spanish, French, Japanese, German, or Portuguese tickets |

### Recommended Role

Use this model as a:

- Department assistant
- Extraction model
- Summarization model
- Domain-tuned classifier
- Lightweight RAG model
- Mid-tier model in a cascade

### Avoid as Sole Model For

- Complex autonomous agents
- Deep policy reasoning
- Long document synthesis that exceeds validated context behavior
- High-risk actions without approval
- Complex API orchestration

### Production Notes

- Treat the `1b` name as a model-family label. Document the exact architecture parameter count separately when procurement, sizing, or governance teams require it.
- Validate against enterprise-specific documents and labels.
- Use retrieval, templates, and schema validation to reduce hallucination risk.
- Use as a middle layer between 350M utility tasks and 3B agentic tasks.

---

## `granite-4.0-h-micro`

### Best Fit

`granite-4.0-h-micro` is a 3B long-context Granite 4.0 model suited for enterprise assistants that need RAG, tool calling, document synthesis, and stronger instruction following than smaller Granite Nano-class deployments, subject to task-specific evaluation.

### Clear Enterprise Use Cases

| Use case | Description | Example |
|---|---|---|
| Enterprise RAG assistant | Answer questions over internal documents | Query HR policies, runbooks, product docs, or engineering knowledge bases |
| Long-context summarization | Summarize large records or multi-turn histories | Summarize an incident timeline or customer escalation history |
| Business copilot | Help employees complete internal workflows | Explain vendor onboarding, access requests, or expense steps |
| IT operations assistant | Interpret logs, alerts, and runbooks | Summarize alert context and recommend the next diagnostic step |
| Customer support copilot | Draft grounded support responses | Use KB articles and ticket context to draft a reply |
| Function-calling assistant | Select and format candidate calls to external tools | Prepare calls to ticketing, asset lookup, CRM, or order-status APIs for validation before execution |
| Code assistant | Help with code completion, explanation, and tests | Explain a service function or draft a unit test |
| Analyst assistant | Combine multiple retrieved sources | Produce an account, incident, or vendor brief |

### Recommended Role

Use this model as a:

- RAG assistant
- Long-context summarizer
- Business copilot
- Tool-calling assistant
- Code helper
- Agent worker model

### Avoid as Sole Model For

- Very cheap high-volume classification where 350M is sufficient
- Hard real-time edge workflows without optimization
- High-risk autonomous actions without policy controls
- Workflows where Granite 4.1 3B has been selected as the enterprise standard

### Production Notes

- Use for long-context and retrieval-heavy workflows.
- Evaluate against Granite 4.1 3B before standardizing.
- Use strict tool schemas and tool-output validation.
- Add observability for retrieval quality, tool calls, and answer grounding.

---

## `granite-4.1-3b`

### Best Fit

`granite-4.1-3b` is the recommended primary candidate within this model set for agentic enterprise AI. It is positioned for AI assistants and LLM agents with tool-use capabilities and has improved post-training for tool calling, instruction following, and chat behavior.

### Clear Enterprise Use Cases

| Use case | Description | Example |
|---|---|---|
| Agentic enterprise assistant | Plan, retrieve, prepare tool calls, and synthesize final responses | Resolve “summarize this account and create a follow-up ticket,” with tool execution gated by policy controls |
| Tool-using IT helpdesk agent | Prepare API calls to support IT workflows | Look up device status, check identity metadata, or create a ticket after permission checks |
| RAG policy assistant | Answer complex questions over internal policy | Explain expense, travel, HR, procurement, or legal policy |
| Workflow automation agent | Turn requests into validated business-action plans | Start vendor onboarding or access approval workflows after deterministic checks |
| Customer support agent | Use KB, CRM, and ticket data | Retrieve customer context and draft a grounded response |
| Software engineering assistant | Help with code explanation, patch planning, and tests | Generate test cases or explain a service change |
| Operations analyst assistant | Synthesize operational context | Combine alerts, logs, runbooks, owners, and prior incidents |
| Long-context document QA | Answer questions across long documents | Analyze contracts, audit reports, architecture docs, or incident retrospectives |
| Agent orchestrator | Coordinate smaller models and tools | Use 350M for routing, 1B for extraction, and 3B for reasoning |

### Recommended Role

Use this model as a:

- Primary enterprise agent model
- RAG answer generator
- Tool-use planner
- Workflow automation assistant
- Policy assistant
- Code and operations assistant
- Orchestrator over smaller specialist models

### Avoid as Sole Model For

- Extremely high-volume classification where 350M is sufficient
- Simple extraction where 1B is cheaper and easier to operate
- Edge workflows without runtime optimization
- Regulated actions without approval, logging, and deterministic controls

### Production Notes

- Use explicit tool schemas.
- Validate tool arguments before execution.
- Implement permission checks outside the model.
- Log retrieval inputs, tool calls, model outputs, and human overrides.
- Use evaluation sets for routing, answer grounding, tool-call accuracy, refusal behavior, and multilingual quality.

---

## Recommended Enterprise Patterns

## Pattern 1: Cost-Optimized Model Cascade

| Layer | Model | Responsibility |
|---|---|---|
| Utility layer | `granite-4.0-h-350m` | Classify, route, filter, validate, extract simple fields |
| Workhorse layer | `granite-4.0-h-1b` | Summarize, enrich, extract complex fields, answer common questions |
| Agentic layer | `granite-4.1-3b` | Plan, reason, use tools, synthesize final responses |
| Control layer | Rules, retrieval, policy engine | Enforce permissions, grounding, auditability, and escalation |

## Pattern 2: Enterprise RAG Assistant

| Component | Recommended model | Role |
|---|---|---|
| Domain classifier | `granite-4.0-h-350m` | Route the query to the correct knowledge domain |
| Query rewriter | `granite-4.0-h-1b` | Improve retrieval queries |
| Chunk filter | `granite-4.0-h-350m` | Remove irrelevant retrieved chunks |
| Answer generator | `granite-4.1-3b` | Produce grounded final response |
| Tool caller | `granite-4.1-3b` | Call approved APIs when needed |
| Safety reviewer | Rules plus `granite-4.0-h-1b` | Flag risky outputs for review |

## Pattern 3: Agentic Workflow Automation

| Agent role | Recommended model | Example responsibility |
|---|---|---|
| Router | `granite-4.0-h-350m` | Determine whether the request belongs to HR, IT, finance, procurement, or legal |
| Extractor | `granite-4.0-h-1b` | Extract requester, dates, IDs, vendor names, and approval fields |
| Planner | `granite-4.1-3b` | Determine the next steps and required tools |
| Tool-use executor | `granite-4.1-3b` | Prepare calls to ticketing, CRM, IAM, ERP, or knowledge systems for validation and execution by trusted services |
| Summarizer | `granite-4.0-h-micro` or `granite-4.1-3b` | Produce user-facing status, rationale, and next steps |

---

## Production Controls

| Control | Requirement |
|---|---|
| Evaluation | Build task-specific evaluation sets for classification, extraction, RAG, tool calls, multilingual behavior, and refusals |
| Grounding | Require retrieved evidence for policy, legal, HR, finance, and support answers |
| Tool safety | Validate tool arguments before execution, enforce permissions outside the model, and treat model-generated tool calls as proposals until approved by trusted services |
| Escalation | Escalate low-confidence, high-risk, or policy-sensitive outputs to humans |
| Observability | Log prompts, retrieved chunks, tool calls, tool results, model outputs, and user feedback |
| Data governance | Apply tenant isolation, PII handling, retention controls, and access controls |
| Runtime fallback | Use fallback models, deterministic rules, or human review when confidence is low |
| Red teaming | Test prompt injection, data leakage, unsafe actions, and multilingual failure modes |
| Versioning | Track model version, prompt version, tool schema version, and retrieval index version |

---

## Selection Rules

| Requirement | Recommended model |
|---|---|
| Lowest cost | `granite-4.0-h-350m` |
| Lowest latency | `granite-4.0-h-350m` |
| Edge or on-device candidate | `granite-4.0-h-350m` |
| High-volume classification | `granite-4.0-h-350m` |
| Structured extraction | `granite-4.0-h-1b` |
| Short summarization | `granite-4.0-h-1b` |
| Domain-specific fine-tuning | `granite-4.0-h-1b` |
| Granite 4.0 long-context assistant | `granite-4.0-h-micro` |
| Enterprise RAG | `granite-4.1-3b` |
| Tool-using agent | `granite-4.1-3b` |
| Workflow automation | `granite-4.1-3b` |
| Long-context synthesis | `granite-4.1-3b` or `granite-4.0-h-micro` |
| Code assistance | `granite-4.1-3b` or `granite-4.0-h-micro` |

---

## Recommended Portfolio

Use the models as a portfolio rather than selecting only one:

1. Use `granite-4.0-h-350m` for routing, classification, filtering, simple extraction, and edge-oriented utility tasks.
2. Use `granite-4.0-h-1b` for structured extraction, short summarization, ticket enrichment, domain-tuned classification, and lightweight RAG.
3. Use `granite-4.0-h-micro` for Granite 4.0 long-context assistant workloads, RAG, document QA, tool-enabled business assistants, and code assistance.
4. Use `granite-4.1-3b` as the preferred candidate for agentic AI, tool-use workflows, enterprise RAG, workflow automation, and production assistant experiences.

## Final Recommendation

For production enterprise agentic AI within the four models covered by this guide, start with `granite-4.1-3b` as the primary candidate for reasoning, retrieval synthesis, and tool-use planning.

Pair it with `granite-4.0-h-350m` and `granite-4.0-h-1b` for lower-cost routing, extraction, classification, and validation.

Use `granite-4.0-h-micro` where Granite 4.0 compatibility, 128K long-context behavior, or deployment standardization on Granite 4.0 is required.

> [!CAUTION]
> Do not treat any model-card capability as a production guarantee. Validate every target workflow with enterprise-specific data, tool schemas, safety tests, and human escalation paths before deployment.

## Revision Notes

This revision resolves the validation findings by:

- Adding an explicit validation basis and separating model-card evidence from benchmark-backed conclusions.
- Clarifying that `granite-4.0-h-1b` is a family label and that exact architecture parameter counts should be documented separately where required.
- Replacing the broader phrase “agentic software engineering” with “software engineering assistance with tool and human review.”
- Adding a multilingual evaluation caveat.
- Treating tool calls as model-generated proposals that must be validated and authorized by trusted services before execution.
- Qualifying the final recommendation as applying within the four models covered by this guide.

## Source References

- IBM Granite 4.0 H 350M model card: <https://huggingface.co/ibm-granite/granite-4.0-h-350m>
- IBM Granite 4.0 H 1B model card: <https://huggingface.co/ibm-granite/granite-4.0-h-1b>
- IBM Granite 4.0 H Micro model card: <https://huggingface.co/ibm-granite/granite-4.0-h-micro>
- IBM Granite 4.1 3B model card: <https://huggingface.co/ibm-granite/granite-4.1-3b>
- IBM Granite 4.1 documentation: <https://www.ibm.com/granite/docs/models/granite4-1>
