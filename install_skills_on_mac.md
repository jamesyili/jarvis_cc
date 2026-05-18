# Install Public Claude Code Skills on Mac

Generated 2026-05-18. Installs publicly-available Claude Code skill collections on a fresh Mac. Does **not** sync any of your personal/private skills.

## Summary — what gets installed

| Source | Skills | Install method |
|--------|--------|----------------|
| [Matt Pocock](https://github.com/mattpocock/skills) | **11 selected** (10 engineering + `grill-me`) | `npx skills@latest` (deselect the rest at the prompt) |
| [Humanizer](https://github.com/blader/humanizer) by blader | 1 | `git clone` |
| [Everything Claude Code (ECC)](https://github.com/affaan-m/everything-claude-code) by Affaan Mustafa | 232 skills + 48 agents + 60 slash commands + hooks | Plugin marketplace |

**Total skills landing in `~/.claude/`: 244** (11 + 1 + 232). Plus all of ECC's agents, commands, and hooks.

For broader discovery: [awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills).

---

## Prerequisites

1. **Claude Code installed on Mac** — verify with `claude --version`. If missing: https://docs.claude.com/en/docs/claude-code/setup
2. **Node.js** — `node --version` should print v18+. Install via `brew install node`.
3. **Git** — `git --version`.

---

## Step 1 — Matt Pocock (11 skills)

From terminal:

```bash
npx skills@latest add mattpocock/skills
```

When the installer prompts you to select skills, **check exactly these 11 and uncheck everything else**:

### Engineering (all 10)
1. `diagnose` — root-cause investigation
2. `grill-with-docs` — grilling against your project's domain model + existing docs
3. `triage` — sort issues / inbox by priority
4. `improve-codebase-architecture` — architectural refactor passes
5. `setup-matt-pocock-skills` — one-time config (required)
6. `tdd` — red-green-refactor TDD loop
7. `to-issues` — break plans into independently-grabbable GitHub issues
8. `to-prd` — turn a rough spec into a PRD
9. `zoom-out` — pull back from tactical noise to product-level framing
10. `prototype` — quick-and-dirty prototyping mode

### Productivity (1 only)
11. `grill-me` — relentless plan/design interrogation

### Deliberately skipped
- Productivity: `caveman`, `handoff`, `write-a-skill`
- Misc: `git-guardrails-claude-code`, `migrate-to-shoehorn`, `scaffold-exercises`, `setup-pre-commit`

Pick Claude Code as the agent at the prompt. After install, in Claude Code:

```
/setup-matt-pocock-skills
```

This walks you through:
- Issue tracker preference (GitHub / Linear / local files)
- Triage label vocabulary
- Documentation save location

---

## Step 2 — Humanizer (1 skill)

```bash
mkdir -p ~/src
git clone https://github.com/blader/humanizer.git ~/src/humanizer
ln -s ~/src/humanizer ~/.claude/skills/humanizer
# Update later with: git -C ~/src/humanizer pull
```

What it does: detects 24 AI writing patterns (em dash overuse, "delve/tapestry/landscape" vocabulary, rule of three, sycophantic tone, negative parallelisms) and rewrites them out. Based on Wikipedia's "Signs of AI writing" guide.

---

## Step 3 — Everything Claude Code (232 skills + agents + hooks)

Inside a Claude Code session:

```
/plugin marketplace add https://github.com/affaan-m/everything-claude-code
/plugin install ecc@ecc
```

That installs the agents, skills, commands, and hooks via the plugin system.

### Optional: install ECC's rules

The plugin route doesn't auto-install ECC's rule packs. If you want them:

```bash
git clone https://github.com/affaan-m/everything-claude-code ~/src/everything-claude-code

mkdir -p ~/.claude/rules/ecc
cp -r ~/src/everything-claude-code/rules/common ~/.claude/rules/ecc/
cp -r ~/src/everything-claude-code/rules/typescript ~/.claude/rules/ecc/
# Copy only the rule folders you actually want — there are more in the repo.
```

### Fallback: manual install via `install.sh`

If the plugin route gives you trouble:

```bash
cd ~/src/everything-claude-code
./install.sh --profile minimal   # excludes hooks-runtime
./install.sh --profile core      # agents + commands + skills, no hooks
./install.sh --profile full      # everything including hooks
```

**Pick one route only** — don't run both `/plugin install` and `./install.sh`.

**Name collision warning**: ECC ships its own `tdd-workflow`, `eval-harness`, `api-design`, `backend-patterns`, `frontend-patterns`, `design-system`, `content-engine`, `crosspost`, `brand-voice`, `council`, `blueprint`, `cost-aware-llm-pipeline`, `data-scraper-agent`, `deep-research`, `fal-ai-media`, `videodb`, `video-editing`, `product-lens` and more. These overlap with skills you already have. Plugin-scoped wins inside their plugin context; user-global wins everywhere else.

---

## Step 4 — Verify

In a fresh Claude Code session:

```
/help
```

Expected highlights:
- From Matt Pocock: `/tdd`, `/grill-me`, `/grill-with-docs`, `/triage`, `/to-issues`, `/diagnose`, `/zoom-out`, `/to-prd`, `/improve-codebase-architecture`, `/prototype`
- From Humanizer: `/humanizer`
- From ECC: a large set of `/`-commands

On disk:

```bash
ls ~/.claude/skills/        # Matt Pocock (11) + Humanizer
ls ~/.claude/plugins/       # ECC plugin
```

---

## Notes & gotchas

- **No personal/private skills are synced.** Your WSL `~/.claude/skills/` Leo-specific skills are excluded intentionally.
- **Updates**:
  - Matt Pocock: re-run `npx skills@latest add mattpocock/skills`
  - Humanizer: `git -C ~/src/humanizer pull`
  - ECC: `/plugin update` inside Claude Code (or `git pull` if you used `install.sh`)
- **MCP servers**: Some skills reference MCP tools (firecrawl, exa, etc.) — install those individually as needed.

---

## TL;DR cheat sheet

```bash
brew install node git

# Matt Pocock — deselect everything except the 11 listed above
npx skills@latest add mattpocock/skills

# Humanizer
git clone https://github.com/blader/humanizer.git ~/src/humanizer
ln -s ~/src/humanizer ~/.claude/skills/humanizer

# ECC — in Claude Code:
# /plugin marketplace add https://github.com/affaan-m/everything-claude-code
# /plugin install ecc@ecc
# /setup-matt-pocock-skills
```

---

## Appendix — Full ECC skill list (232)

Fetched from `github.com/affaan-m/everything-claude-code/skills/` on 2026-05-18 via GitHub API.

```
accessibility                          agent-architecture-audit
agent-eval                             agent-harness-construction
agent-introspection-debugging          agent-payment-x402
agent-sort                             agentic-engineering
agentic-os                             ai-first-engineering
ai-regression-testing                  android-clean-architecture
angular-developer                      api-connector-builder
api-design                             architecture-decision-records
article-writing                        automation-audit-ops
autonomous-agent-harness               autonomous-loops
backend-patterns                       benchmark
blender-motion-state-inspection        blueprint
brand-voice                            browser-qa
bun-runtime                            canary-watch
carrier-relationship-management        cisco-ios-patterns
ck                                     claude-devfleet
click-path-audit                       clickhouse-io
code-tour                              codebase-onboarding
coding-standards                       compose-multiplatform-patterns
configure-ecc                          connections-optimizer
content-engine                         content-hash-cache-pattern
context-budget                         continuous-agent-loop
continuous-learning                    continuous-learning-v2
cost-aware-llm-pipeline                cost-tracking
council                                cpp-coding-standards
cpp-testing                            crosspost
csharp-testing                         customer-billing-ops
customs-trade-compliance               dart-flutter-patterns
dashboard-builder                      data-scraper-agent
database-migrations                    deep-research
defi-amm-security                      deployment-patterns
design-system                          django-celery
django-patterns                        django-security
django-tdd                             django-verification
dmux-workflows                         docker-patterns
documentation-lookup                   dotnet-patterns
e2e-testing                            ecc-guide
ecc-tools-cost-audit                   email-ops
energy-procurement                     enterprise-agent-ops
error-handling                         eval-harness
evm-token-decimals                     exa-search
fal-ai-media                           fastapi-patterns
finance-billing-ops                    flox-environments
flutter-dart-code-review               foundation-models-on-device
frontend-design-direction              frontend-patterns
frontend-slides                        fsharp-testing
gan-style-harness                      gateguard
git-workflow                           github-ops
golang-patterns                        golang-testing
google-workspace-ops                   healthcare-cdss-patterns
healthcare-emr-patterns                healthcare-eval-harness
healthcare-phi-compliance              hermes-imports
hexagonal-architecture                 hipaa-compliance
homelab-network-readiness              homelab-network-setup
homelab-pihole-dns                     homelab-vlan-segmentation
homelab-wireguard-vpn                  hookify-rules
inventory-demand-planning              investor-materials
investor-outreach                      ios-icon-gen
iterative-retrieval                    java-coding-standards
jira-integration                       jpa-patterns
knowledge-ops                          kotlin-coroutines-flows
kotlin-exposed-patterns                kotlin-ktor-patterns
kotlin-patterns                        kotlin-testing
laravel-patterns                       laravel-plugin-discovery
laravel-security                       laravel-tdd
laravel-verification                   lead-intelligence
liquid-glass-design                    llm-trading-agent-security
logistics-exception-management         make-interfaces-feel-better
manim-video                            market-research
mcp-server-patterns                    messages-ops
mle-workflow                           motion-advanced
motion-foundations                     motion-patterns
motion-ui                              mysql-patterns
nanoclaw-repl                          nestjs-patterns
netmiko-ssh-automation                 network-bgp-diagnostics
network-config-validation              network-interface-health
nextjs-turbopack                       nodejs-keccak256
nutrient-document-processing           nuxt4-patterns
openclaw-persona-forge                 opensource-pipeline
perl-patterns                          perl-security
perl-testing                           plan-orchestrate
plankton-code-quality                  postgres-patterns
prisma-patterns                        product-capability
product-lens                           production-audit
production-scheduling                  project-flow-ops
prompt-optimizer                       python-patterns
python-testing                         pytorch-patterns
quality-nonconformance                 quarkus-patterns
quarkus-security                       quarkus-tdd
quarkus-verification                   ralphinho-rfc-pipeline
recsys-pipeline-architect              redis-patterns
regex-vs-llm-structured-text           remotion-video-creation
repo-scan                              research-ops
returns-reverse-logistics              rules-distill
rust-patterns                          rust-testing
safety-guard                           santa-method
scientific-db-pubmed-database          scientific-db-uspto-database
scientific-pkg-gget                    scientific-thinking-literature-review
scientific-thinking-scholar-evaluation search-first
security-bounty-hunter                 security-review
security-scan                          seo
skill-comply                           skill-scout
skill-stocktake                        social-graph-ranker
springboot-patterns                    springboot-security
springboot-tdd                         springboot-verification
strategic-compact                      swift-actor-persistence
swift-concurrency-6-2                  swift-protocol-di-testing
swiftui-patterns                       tdd-workflow
team-builder                           terminal-ops
tinystruct-patterns                    token-budget-advisor
ui-demo                                ui-to-vue
uncloud                                unified-notifications-ops
verification-loop                      video-editing
videodb                                visa-doc-translate
vite-patterns                          windows-desktop-e2e
workspace-surface-audit                x-api
```
