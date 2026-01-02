# Mission Statement: The Assembly-First Prototyping Engine

### The Problem

Traditional LLM-based frontend generation (like raw Vercel v0 clones) suffers from the **"Entropy Tax."** As complexity grows, the LLM spends more tokens on boilerplate CSS, accessibility attributes, and basic state management, leading to:

1. **Token Waste:** 80% of generated code is repetitive layout and primitive logic.
2. **Inconsistency:** Buttons, inputs, and modals drift in style and behavior across iterations.
3. **Fragility:** LLMs frequently fail at complex ARIA patterns and "z-index" management.

### The Vision

We are transitioning from **generating code** to **orchestrating a design system.** By utilizing **React Aria** as our foundational layer and **Storybook** as our living documentation, we provide Claude with a high-level "vocabulary" of production-ready components.

Our goal is a system where the AI acts as a **Senior UI Engineer** who knows our library intimately—focusing its reasoning power on **data flow, business logic, and user experience** rather than the intricacies of a `ComboBox` implementation.

---

# Execution Plan: The "Skill-Based" Design System

### Phase 1: The Component Core (React Aria + Tailwind)

We will build a "Headless-First" library. We don't want a "black box" library; we want accessible primitives that are easy for an AI to style if needed.

* **Source:** Use `react-aria-components` (the high-level library) rather than just the hooks for faster assembly.
* **Styling:** Use **Tailwind CSS** with a strict set of design tokens (colors, spacing) defined in `tailwind.config.js`.
* **The "Clean" Rule:** Components must accept standard props (`className`, `style`, `children`) and follow the React Aria naming conventions.

### Phase 2: Storybook as the Source of Truth

Storybook is not just for developers; it is the **LLM's training manual.**

* **Atomic Stories:** Every component must have a `.stories.tsx` file demonstrating all variants (e.g., `Loading`, `Error`, `Disabled`).
* **Documentation Blocks:** Use Storybook's `Autodocs`. The AI will read the **ArgsTable** to understand which props it can pass.
* **Static Manifest:** Export a `component-manifest.json` from Storybook. This file maps component names to their prop types and usage examples.

### Phase 3: Packaging into Claude Code Skills

We will create a specific directory structure in `.claude/skills/ui-engine/` to enable "Component Awareness."

```text
.claude/skills/ui-engine/
├── SKILL.md             # The "Master Instructions" for component usage
├── manifests/           # JSON files describing components and their props
│   └── components.json
├── templates/           # Multi-component patterns (e.g., "Login Screen", "Data Grid")
│   └── dashboard_layout.tsx
└── examples/            # High-quality "Golden Samples" of assembly
    └── data_fetching_page.tsx

```

### Phase 4: The AI Instruction Logic (Exactness)

In the `SKILL.md`, we will define the **Strict Usage Protocol**:

1. **Discovery:** Before writing any UI code, the agent MUST read `manifests/components.json`.
2. **Constraint:** The agent is FORBIDDEN from writing raw `<input>` or `<div>` buttons if a library component exists.
3. **Implementation:** The agent writes the "Glue Code" (e.g., `useQuery` for your non-mocked data) and passes that data into the pre-made templates.
4. **Token Optimization:** Instructions will tell the AI: *"Do not re-implement CSS. Use the component and only provide override classes for layout positioning."*

---

### Critical Analysis: Why this wins

* **Token Savings:** You reduce a 2,000-token prompt for a "Searchable Dropdown" to a 50-token instruction: `<SearchCombo items={data} />`.
* **Accessibility (A11y) by Default:** React Aria handles the complex keyboard navigation and screen reader support that LLMs almost always hallucinate or ignore.
* **Data Integration:** Since you are using non-mocked data, the AI can focus 100% on the **Hook logic** (fetching, filtering, sorting) and simply "plug" the results into the components.

