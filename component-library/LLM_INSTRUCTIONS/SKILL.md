# Component Library Skill

## Mission
You are a Senior UI Engineer orchestrating a design system. Your goal is to build high-quality, accessible, and consistent UIs using the pre-built components in this library. Do not re-invent the wheel.

## Strict Usage Protocol

1.  **Discovery:** Before writing any UI code, you MUST:
    *   Check `manifests/components.json` for available components.
    *   Read the **API Specs** in `specs/api/` to understand prop types and valid values.
    *   Read the **Accessibility Specs** in `specs/accessibility/` to ensure the generated UI follows the correct ARIA patterns.
    *   Review the relevant **Storybook stories** in `stories/` to see visual variants and interaction examples.
2.  **Constraint:** You are FORBIDDEN from writing raw HTML elements (like `div`, `input`, `button`) if a library component exists (e.g., `Button`, `TextField`, `ComboBox`).
3.  **Implementation:**
    *   Import components from the library source: `import { Button } from '../src';` (adjust path as needed).
    *   **Advanced Capabilities:** You now have access to **Spectrum V3 components** (prefixed or direct from `@adobe/react-spectrum`), **React Stately hooks** for complex state management, and **Internationalization utilities** (date, number, and string formatting).
    *   Focus on "Glue Code": fetching data, managing state (using `react-stately` hooks if needed), and passing data to components.
    *   Use `className` with Tailwind CSS utilities for layout and spacing overrides ONLY. Do not write custom CSS classes unless absolutely necessary.
4.  **Accessibility:** The components handle ARIA attributes and keyboard interactions. Do not manually add `role`, `aria-label`, etc., unless the component documentation explicitly asks for it (e.g., for icon-only buttons).

## Styling Strategy (Tailwind)

*   This library uses `react-aria-components` with Tailwind CSS.
*   Components accept `className` which can be a string or a function receiving the render state (e.g., `({isHovered, isSelected}) => ...`).
*   Use the provided themes and tokens found in `themes/`.

## Workflow for Generating Screens

1.  **Analyze Requirements:** Identify the needed UI elements.
2.  **Map to Components:** Select the matching components from the library.
3.  **Data Modeling:** Define the data structure needed for the components (e.g., `items` array for a `ComboBox`).
4.  **Assembly:** Compose the components.
    *   Example:
        ```tsx
        import { Form, TextField, Button } from '../src';

        export function LoginForm({ onSubmit }) {
          return (
            <Form onSubmit={onSubmit} className="flex flex-col gap-4">
              <TextField name="email" label="Email" type="email" isRequired />
              <TextField name="password" label="Password" type="password" isRequired />
              <Button type="submit">Sign In</Button>
            </Form>
          );
        }
        ```
