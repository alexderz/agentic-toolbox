# Modern Web Guidance index

One row per guide: id, path, one line. Pick rows that match the task,
then read each chosen guide in full. Never read the whole catalog. How
to use it: [SKILL.md](SKILL.md#lookup).

Descriptions are adapted from the upstream README at the pin
(Apache-2.0), except six toolbox-written lines for the guides that
README omits. Guides are CC-BY-4.0: [guides/NOTICE.md](guides/NOTICE.md).

209 guides.

## accessibility

| Id | Path | Description |
| --- | --- | --- |
| `accessibility` | [guides/accessibility/accessibility.md](guides/accessibility/accessibility.md) | Broad accessibility rules for any UI: structure, semantics and ARIA, names, keyboard and focus, media, forms, live regions, color, motion and testing. |
| `accessible-error-announcement` | [guides/accessibility/accessible-error-announcement.md](guides/accessibility/accessible-error-announcement.md) | Synchronize programmatic accessibility states (like aria-invalid) with the visual :user-invalid state to ensure screen reader users receive error feedback only after interaction, mirroring the visual experience. |
| `accessible-generated-content` | [guides/accessibility/accessible-generated-content.md](guides/accessibility/accessible-generated-content.md) | Use CSS generated content (`::before`/`::after`) in ways that stay accessible, including alternative text for decorative content. |
| `respect-os-text-scale` | [guides/accessibility/respect-os-text-scale.md](guides/accessibility/respect-os-text-scale.md) | Respect the operating system's text scale preference for a page so font sizes, layout, and rem-based measurements follow the user's accessibility settings. |

## built-in-ai

| Id | Path | Description |
| --- | --- | --- |
| `language-detection` | [guides/built-in-ai/language-detection.md](guides/built-in-ai/language-detection.md) | Detect the language of user-generated content or already present site content. |
| `language-model` | [guides/built-in-ai/language-model.md](guides/built-in-ai/language-model.md) | Run on-device natural language inference in the browser using the Prompt API, with streaming output, structured JSON responses, and multi-turn session management. |
| `prompt-api` | [guides/built-in-ai/prompt-api.md](guides/built-in-ai/prompt-api.md) | Prompt API with Gemini Nano: on-device prompting, streaming, structured output and sessions. Same topic as `language-model`. |
| `summarizer` | [guides/built-in-ai/summarizer.md](guides/built-in-ai/summarizer.md) | Summarize text content using the on-device Summarizer API. |
| `translator` | [guides/built-in-ai/translator.md](guides/built-in-ai/translator.md) | Translate text between languages using the on-device Translator API. |

## css

| Id | Path | Description |
| --- | --- | --- |
| `animate-to-intrinsic-sizes` | [guides/css/animate-to-intrinsic-sizes.md](guides/css/animate-to-intrinsic-sizes.md) | Smoothly animate interactive components (like accordions, menus, and expanding cards) to and from their natural dimensions. |
| `atrule-support-conditionals` | [guides/css/atrule-support-conditionals.md](guides/css/atrule-support-conditionals.md) | Conditionally apply certain CSS rules or declarations only if a certain at-rule is supported by the browser. |
| `calculate-with-intrinsic-sizes` | [guides/css/calculate-with-intrinsic-sizes.md](guides/css/calculate-with-intrinsic-sizes.md) | Calculate the size of an element based on its intrinsic size, while ensuring it fits within given design constraints. |
| `child-state-based-styling` | [guides/css/child-state-based-styling.md](guides/css/child-state-based-styling.md) | Build a component that changes its styling based on the state of one of its child elements. |
| `content-based-styling` | [guides/css/content-based-styling.md](guides/css/content-based-styling.md) | Build a component that changes its layout based on whether it contains specific child elements (or not). |
| `css-layout` | [guides/css/css-layout.md](guides/css/css-layout.md) | Modern CSS layouts such as flexbox, grid, subgrid, container queries, anchor positioning, and intrinsic sizing. |
| `css` | [guides/css/css.md](guides/css/css.md) | Action-oriented guidelines for modern CSS architecture, including the cascade, selectors, scoping, nesting, and design tokens. |
| `design-token-reactivity` | [guides/css/design-token-reactivity.md](guides/css/design-token-reactivity.md) | Define higher-order design tokens, like density modes (compact, comfortable, spacious) or themes and have descendant components react to changes directly and in component-appropriate ways. |
| `dynamic-sibling-styling` | [guides/css/dynamic-sibling-styling.md](guides/css/dynamic-sibling-styling.md) | Create dynamic visual spectrums or layout arrangements that automatically adapt to the number of elements in a group. |
| `fluid-scaling` | [guides/css/fluid-scaling.md](guides/css/fluid-scaling.md) | Scale items like font size, spacing, and media sizes smoothly based on the parent container's size rather than using fixed breakpoints |
| `individual-transform-properties` | [guides/css/individual-transform-properties.md](guides/css/individual-transform-properties.md) | Animate or override individual CSS transform properties (e.g. |
| `overflow-clipping-control` | [guides/css/overflow-clipping-control.md](guides/css/overflow-clipping-control.md) | Adjust the visible clipping boundary of an element to align with the content edge, padding edge, or border edge—or a specified offset from any of these—offering finer-grained control over how content is clipped. |
| `reduce-style-repetition` | [guides/css/reduce-style-repetition.md](guides/css/reduce-style-repetition.md) | Reduce excessive style repetition by encapsulating complex or dynamic styling logic into reusable functions (such as a function that computes a gradient based on a set of input parameters). |
| `responsive-design` | [guides/css/responsive-design.md](guides/css/responsive-design.md) | Build UI that adapts to container and viewport size, including container queries, dynamic viewport units, aspect ratios, and responsive typography. |
| `selector-atrule-combinations` | [guides/css/selector-atrule-combinations.md](guides/css/selector-atrule-combinations.md) | Target elements based on the intersection or union of selectors and conditional @-rules while minimizing repetition. |
| `size-aware-styling` | [guides/css/size-aware-styling.md](guides/css/size-aware-styling.md) | Build a component whose styles can be conditionally dependent on its own width or height, rather than the width or height of the viewport. |
| `style-parent-with-has` | [guides/css/style-parent-with-has.md](guides/css/style-parent-with-has.md) | Style parent elements of a form field (e.g. |
| `usage-aware-component-variations` | [guides/css/usage-aware-component-variations.md](guides/css/usage-aware-component-variations.md) | Build components that adapt visual logic based on semantic context using CSS container style queries. |

## forms

| Id | Path | Description |
| --- | --- | --- |
| `animated-select-picker` | [guides/forms/animated-select-picker.md](guides/forms/animated-select-picker.md) | Create a custom select component whose dropdown is animated. |
| `autofill-address-form` | [guides/forms/autofill-address-form.md](guides/forms/autofill-address-form.md) | Build an address form with correct autocomplete attributes and autofill support. |
| `autofill-highlight-inputs` | [guides/forms/autofill-highlight-inputs.md](guides/forms/autofill-highlight-inputs.md) | Customize the styling of form fields that have been autofilled and not edited by the user |
| `autofill-payment-form` | [guides/forms/autofill-payment-form.md](guides/forms/autofill-payment-form.md) | Build a payment form that collects card details with correct autocomplete values and autofill support. |
| `autofill-sign-in-form` | [guides/forms/autofill-sign-in-form.md](guides/forms/autofill-sign-in-form.md) | Build a sign-in form with correct autocomplete values and autofill support. |
| `autofill-sign-up-form` | [guides/forms/autofill-sign-up-form.md](guides/forms/autofill-sign-up-form.md) | Build a sign-up form with correct autocomplete values and autofill support. |
| `brand-consistent-forms` | [guides/forms/brand-consistent-forms.md](guides/forms/brand-consistent-forms.md) | Match checkboxes, radio buttons, range sliders, and progress bars to your site's color palette without replacing them with custom components. |
| `branded-select-styling` | [guides/forms/branded-select-styling.md](guides/forms/branded-select-styling.md) | Create custom select elements whose button, picker, arrow icon, and checkmark all seamlessly match your brand or design system's typography, colors, spacing, and border treatments. |
| `custom-select-picker-layouts` | [guides/forms/custom-select-picker-layouts.md](guides/forms/custom-select-picker-layouts.md) | Create custom select pickers whose options are positioned in unique or interesting ways, rather than the traditional stacked list of options. |
| `form-fields-automatically-fit-contents` | [guides/forms/form-fields-automatically-fit-contents.md](guides/forms/form-fields-automatically-fit-contents.md) | Allow form fields to grow and shrink to fit the user input, e.g. |
| `forms` | [guides/forms/forms.md](guides/forms/forms.md) | Broad form rules: structure, labels, autofill, validation, styling, script submission, identity and payments, addresses and multi-page forms. |
| `ime-safe-enter-submit` | [guides/forms/ime-safe-enter-submit.md](guides/forms/ime-safe-enter-submit.md) | Implement Enter-to-submit in textareas and single-line inputs (chat, search, inline rename) safely for IME (Input Method Editor) users to prevent submitting incomplete text. |
| `required-field-feedback` | [guides/forms/required-field-feedback.md](guides/forms/required-field-feedback.md) | Provide error message for required form fields that were skipped or left empty *only* after user interaction, to avoid preemptive errors and ensure feedback is timely and contextually relevant to the user's flow. |
| `rich-media-picker` | [guides/forms/rich-media-picker.md](guides/forms/rich-media-picker.md) | Create a custom select component whose options can contain complex HTML formatting (e.g. |
| `select-menu-interaction` | [guides/forms/select-menu-interaction.md](guides/forms/select-menu-interaction.md) | Validate that a non-default option has been chosen in a select menu only after the user has interacted with the control. |
| `slider` | [guides/forms/slider.md](guides/forms/slider.md) | Style a native range slider with custom track, thumb, fill, and focus states while preserving native functionality and accessibility. |
| `sms-otp-form` | [guides/forms/sms-otp-form.md](guides/forms/sms-otp-form.md) | Verify user phone numbers and one-time passcodes delivered over SMS with automatic code extraction and accessible form input. |
| `switch` | [guides/forms/switch.md](guides/forms/switch.md) | Build an accessible switch with the native HTML switch attribute, falling back to a styled checkbox when not supported. |
| `validate-input-after-interaction` | [guides/forms/validate-input-after-interaction.md](guides/forms/validate-input-after-interaction.md) | Show form field validation feedback (e.g. |

## html

| Id | Path | Description |
| --- | --- | --- |
| `accessible-web-components` | [guides/html/accessible-web-components.md](guides/html/accessible-web-components.md) | Make custom elements accessible by default, setting roles and ARIA state via the ElementInternals ARIA mixin, managing focus with delegatesFocus, and keeping ARIA relationships within a single shadow root. |
| `custom-elements` | [guides/html/custom-elements.md](guides/html/custom-elements.md) | Define, register, and manage the lifecycle of autonomous custom elements, covering constructor rules, lifecycle callbacks, upgrade timing, attribute/property reflection, and naming conventions. |
| `form-associated-custom-elements` | [guides/html/form-associated-custom-elements.md](guides/html/form-associated-custom-elements.md) | Make a custom control participate natively in forms with formAssociated and ElementInternals, submitting its own value, integrating with constraint validation, and reacting to reset, disable, and state-restore. |
| `html` | [guides/html/html.md](guides/html/html.md) | Broad HTML rules: semantics, content grouping, resource priority, dialogs and popovers, disclosures, focus, media and interactivity. |
| `prerendering-custom-elements` | [guides/html/prerendering-custom-elements.md](guides/html/prerendering-custom-elements.md) | Server-render a custom element, then hydrate it in place without re-rendering or a flash of unstyled content. |
| `shadow-dom` | [guides/html/shadow-dom.md](guides/html/shadow-dom.md) | Encapsulate a component's DOM and styles with Shadow DOM, construct the tree efficiently with HTML templates, and project consumer content with slots. |
| `styling-web-components` | [guides/html/styling-web-components.md](guides/html/styling-web-components.md) | Style across the shadow boundary with :host selectors, inherited and custom properties for theming, ::slotted and ::part, and cascade layers and container queries inside components. |
| `web-components` | [guides/html/web-components.md](guides/html/web-components.md) | Orientation and cross-cutting principles for authoring and using Web Components, covering Custom Elements, Shadow DOM, templates and slots, Declarative Shadow DOM, styling across the shadow boundary, Form-Associated Custom Elements, and accessibility requirements. |

## js

| Id | Path | Description |
| --- | --- | --- |
| `calculate-event-differentials` | [guides/js/calculate-event-differentials.md](guides/js/calculate-event-differentials.md) | Calculate elapsed or remaining time between dates and times, balance duration units, and format human-readable localized durations using Temporal.Duration and Intl.DurationFormat. |
| `capture-location-agnostic-data` | [guides/js/capture-location-agnostic-data.md](guides/js/capture-location-agnostic-data.md) | Model location-agnostic calendar dates, wall-clock times, partial dates (recurring birthdays, credit card expirations), and recurring monthly intervals without time zone drift using Temporal Plain types. |
| `coordinate-global-events` | [guides/js/coordinate-global-events.md](guides/js/coordinate-global-events.md) | Schedule future meetings or events by explicitly binding them to a geographical IANA time zone so that event times remain accurate regardless of Daylight Saving Time (DST) transitions, "skipped" or "repeated" hours during clock changes. |
| `sort-high-precision-timestamps` | [guides/js/sort-high-precision-timestamps.md](guides/js/sort-high-precision-timestamps.md) | Parse, sort, and measure intervals between sub-millisecond or nanosecond ISO 8601 timestamps without Date truncation collisions using Temporal.Instant. |
| `support-global-calendar-systems` | [guides/js/support-global-calendar-systems.md](guides/js/support-global-calendar-systems.md) | Display and calculate dates in non-Gregorian calendar systems (e.g., Islamic, Hebrew, or Chinese) accurately for international users. |

## performance

| Id | Path | Description |
| --- | --- | --- |
| `batch-analytics-events` | [guides/performance/batch-analytics-events.md](guides/performance/batch-analytics-events.md) | Debounce and batch multiple analytics, telemetry, and Core Web Vitals events together in a single beacon to minimize network contention and reduce server load, while still delivering real-time updates. |
| `break-up-long-tasks` | [guides/performance/break-up-long-tasks.md](guides/performance/break-up-long-tasks.md) | Break up heavy synchronous processing (complex computations and/or long loops) or DOM updates to improve Interaction to Next Paint (INP) responsiveness and let the browser handle user input and repaint the screen. |
| `calculate-total-foreground-time` | [guides/performance/calculate-total-foreground-time.md](guides/performance/calculate-total-foreground-time.md) | Calculate the total time a user actually spent viewing a page, excluding periods when the tab was in the background. |
| `conditional-async-dependencies` | [guides/performance/conditional-async-dependencies.md](guides/performance/conditional-async-dependencies.md) | Conditionally load or initialize async dependencies (such as importing polyfills for missing web features) without requiring complex orchestration across all of a page's script dependencies. |
| `defer-rendering-heavy-content` | [guides/performance/defer-rendering-heavy-content.md](guides/performance/defer-rendering-heavy-content.md) | Reduce rendering times in content-heavy web pages (e.g. |
| `defer-work-until-scroll-ends` | [guides/performance/defer-work-until-scroll-ends.md](guides/performance/defer-work-until-scroll-ends.md) | Defer expensive operations like DOM updates, data fetching, analytics tracking, or layout recalculation until after scrolling completes to maintain smooth scroll performance. |
| `deliver-optimized-decorative-images` | [guides/performance/deliver-optimized-decorative-images.md](guides/performance/deliver-optimized-decorative-images.md) | Deliver optimized decorative images (such as backgrounds, UI icons, or complex masks) by simultaneously providing next-generation image formats (like AVIF or WebP) alongside multiple pixel densities (like 1x and 2x) so the browser can dynamically negotiate the best combination of file size and visual quality for the user's device capabilities. |
| `deprioritize-background-fetches` | [guides/performance/deprioritize-background-fetches.md](guides/performance/deprioritize-background-fetches.md) | Deprioritize background data fetches made with the Fetch API to prevent network contention with user-initiated requests. |
| `detect-initial-visibility-state` | [guides/performance/detect-initial-visibility-state.md](guides/performance/detect-initial-visibility-state.md) | Reliably determine whether a page was initially loaded in the background, even in cases where the script is loaded asynchronously after the user foregrounded the page. |
| `efficient-background-processing` | [guides/performance/efficient-background-processing.md](guides/performance/efficient-background-processing.md) | Conserve system resources and battery life by pausing background JavaScript execution (such as `&lt;canvas&gt;` animations, WebGL rendering, or high-frequency WebSocket data polling) when the component is off-screen and then resume them just-in-time when they scroll back into view. |
| `faster-spa-view-transitions` | [guides/performance/faster-spa-view-transitions.md](guides/performance/faster-spa-view-transitions.md) | Enable faster transitions back to previously visited views in a Single-Page Application (SPA) by preserving their structural DOM state instead of destroying and rebuilding them on every navigation. |
| `flicker-free-client-side-ab-testing` | [guides/performance/flicker-free-client-side-ab-testing.md](guides/performance/flicker-free-client-side-ab-testing.md) | Deliver and render A/B tests, multi-variate tests, or other experiments using client-side JavaScript to alter or inject HTML, CSS, and JavaScript without the original content showing first before flickering or flashing to show the experiment content. |
| `full-session-analytics` | [guides/performance/full-session-analytics.md](guides/performance/full-session-analytics.md) | Reliably track analytics, Core Web Vitals, errors, and telemetry data across the user's entire page visit, and defer sending of the data until the user leaves the page. |
| `identify-heavy-scripts` | [guides/performance/identify-heavy-scripts.md](guides/performance/identify-heavy-scripts.md) | Identify the scripts most responsible for long animation frames |
| `identify-inp-causes` | [guides/performance/identify-inp-causes.md](guides/performance/identify-inp-causes.md) | Identify slow-running JavaScript and other causes of poor Interaction to Next Paint (INP) responsiveness. |
| `improve-next-page-load-performance` | [guides/performance/improve-next-page-load-performance.md](guides/performance/improve-next-page-load-performance.md) | Improve page load performance by prefetching or prerendering pages that the user is likely to visit next. |
| `interaction-paint-timing` | [guides/performance/interaction-paint-timing.md](guides/performance/interaction-paint-timing.md) | Measure the time it takes for user interactions and client-side navigations to render new contentful updates on screen. |
| `interactions-in-complex-layouts` | [guides/performance/interactions-in-complex-layouts.md](guides/performance/interactions-in-complex-layouts.md) | Make interactions snappier and more responsive (reducing Interaction to Next Paint (INP) scores) by avoiding layout re-calculations in complex layouts, such as data-heavy dashboards or spreadsheet-style grids. |
| `lazy-load-video-and-audio` | [guides/performance/lazy-load-video-and-audio.md](guides/performance/lazy-load-video-and-audio.md) | Defer downloading offscreen video and audio assets, including video poster images and preloaded media data, until the media player approaches the viewport to conserve bandwidth and reduce network contention during initial page load. |
| `optimize-image-priority` | [guides/performance/optimize-image-priority.md](guides/performance/optimize-image-priority.md) | Optimize the loading priority of Largest Contentful Paint (LCP) candidate images and deprioritize non-critical images to reduce critical resource load delays. |
| `optimize-preload-priority` | [guides/performance/optimize-preload-priority.md](guides/performance/optimize-preload-priority.md) | Optimize the relative priority of preloaded content to reduce critical resource load delays. |
| `optimize-script-priority` | [guides/performance/optimize-script-priority.md](guides/performance/optimize-script-priority.md) | Optimize the loading priority of scripts by boosting critical asynchronous scripts and deprioritizing non-essential or late-body scripts to improve sequencing and reduce delays. |
| `out-of-order-html-streaming` | [guides/performance/out-of-order-html-streaming.md](guides/performance/out-of-order-html-streaming.md) | Declaratively update a page with content streamed later into the same HTML document or via imperative JavaScript APIs. |
| `performance` | [guides/performance/performance.md](guides/performance/performance.md) | Broad performance rules: critical rendering path, LCP, INP, third-party scripts, CSS containment, images, caching, fonts, video and code splitting. |
| `resolution-optimized-pseudo-elements` | [guides/performance/resolution-optimized-pseudo-elements.md](guides/performance/resolution-optimized-pseudo-elements.md) | Use resolution-optimized images in CSS pseudo-elements (such as `::before` and `::after`) to reduce the number of DOM nodes. |
| `schedule-tasks-by-priority` | [guides/performance/schedule-tasks-by-priority.md](guides/performance/schedule-tasks-by-priority.md) | Schedule tasks with different priorities to ensure critical work runs first while background work is deferred. |

## privacy

| Id | Path | Description |
| --- | --- | --- |
| `privacy` | [guides/privacy/privacy.md](guides/privacy/privacy.md) | Action-oriented guidelines for web developers to implement privacy by design, data minimization, third-party audits, and secure data handling. |

## pwa

| Id | Path | Description |
| --- | --- | --- |
| `install-web-app` | [guides/pwa/install-web-app.md](guides/pwa/install-web-app.md) | Install web applications from a page using browser-controlled consent UI. |
| `migrate-web-app-origin` | [guides/pwa/migrate-web-app-origin.md](guides/pwa/migrate-web-app-origin.md) | Transfer an installed web app to a new origin while preserving user configuration and OS-level shortcuts. |

## security

| Id | Path | Description |
| --- | --- | --- |
| `client-side-encryption` | [guides/security/client-side-encryption.md](guides/security/client-side-encryption.md) | Establish shared secrets using public-key encapsulation or key agreement—including hybrid and post-quantum protection—and encrypt sensitive data in the browser with authenticated encryption. |
| `digital-signatures` | [guides/security/digital-signatures.md](guides/security/digital-signatures.md) | Sign and verify messages, tokens, or artifacts in the browser using classical or quantum-resistant (post-quantum) asymmetric keys to ensure data integrity and authenticity. |
| `local-network-access` | [guides/security/local-network-access.md](guides/security/local-network-access.md) | Access resources on a user's local network or loopback interface from a public web application. |
| `passkey-authentication` | [guides/security/passkey-authentication.md](guides/security/passkey-authentication.md) | Authenticate a returning user with a passkey for primary sign-in. |
| `passkey-conditional-create` | [guides/security/passkey-conditional-create.md](guides/security/passkey-conditional-create.md) | Silently register a passkey for an existing user after a successful password login. |
| `passkey-management` | [guides/security/passkey-management.md](guides/security/passkey-management.md) | Let users view and manage the passkeys registered to their account. |
| `passkey-reauthentication` | [guides/security/passkey-reauthentication.md](guides/security/passkey-reauthentication.md) | Verify a signed-in user's identity using their existing passkeys before a sensitive action. |
| `passkey-registration` | [guides/security/passkey-registration.md](guides/security/passkey-registration.md) | Register a passkey for an existing user account. |
| `passkeys` | [guides/security/passkeys.md](guides/security/passkeys.md) | Comprehensive orientation and cross-cutting principles for implementing WebAuthn and Passkeys in web applications. |
| `quick-sign-ins` | [guides/security/quick-sign-ins.md](guides/security/quick-sign-ins.md) | Authenticate returning users in place with their saved passkeys or passwords before navigating to a sign-in page or interrupting their workflow. |
| `restrict-outbound-connections` | [guides/security/restrict-outbound-connections.md](guides/security/restrict-outbound-connections.md) | Restrict a page or worker to communicating only with an explicit allowlist of network endpoints to prevent unauthorized third-party requests and client-side data exfiltration. |
| `sanitize-untrusted-html` | [guides/security/sanitize-untrusted-html.md](guides/security/sanitize-untrusted-html.md) | Safely parse and display untrusted HTML content from user input by removing unsafe elements and attributes. |
| `secure-external-subresources` | [guides/security/secure-external-subresources.md](guides/security/secure-external-subresources.md) | Verify the cryptographic integrity of external scripts, stylesheets, fonts, and images loaded from third-party origins, and control whether those requests send credentials or referrer URLs. |
| `security` | [guides/security/security.md](guides/security/security.md) | Broad browser-side defenses in phases: secure contexts, DOM sinks, cookies, framing and messaging, then report-only discovery, CSP, Trusted Types and cross-origin isolation. |
| `trusted-types` | [guides/security/trusted-types.md](guides/security/trusted-types.md) | Prevent DOM-based XSS attacks by defining a Trusted Types policy to sanitize untrusted HTML, using the policy when writing to DOM sinks like innerHTML, and enforcing Trusted Types via Content Security Policy. |
| `validate-origins` | [guides/security/validate-origins.md](guides/security/validate-origins.md) | Compare and validate web origins and sites safely across cross-document messages and URLs without error-prone string parsing. |
| `verify-email-ownership` | [guides/security/verify-email-ownership.md](guides/security/verify-email-ownership.md) | Verify that a user owns an email address during account creation, sign-in, or recovery without sending a one-time passcode or magic link email. **Origin Trial: needs a trial token. Registering for it is an account action; see the entry's Experimental status.** |

## ui-atoms

| Id | Path | Description |
| --- | --- | --- |
| `carousel-slide-effects` | [guides/ui-atoms/carousel-slide-effects.md](guides/ui-atoms/carousel-slide-effects.md) | Create a carousel of slides with images or other visual elements, where each slide animates as they enter/center/exit their scroller. |
| `component-specific-light-dark-theme` | [guides/ui-atoms/component-specific-light-dark-theme.md](guides/ui-atoms/component-specific-light-dark-theme.md) | Force certain elements to be in light mode or dark mode (e.g. |
| `icons` | [guides/ui-atoms/icons.md](guides/ui-atoms/icons.md) | Display and manage icons that can be set and parameterized from CSS, are fast to load, crisp at any resolution and are properly exposed to (or hidden from) assistive technologies. |
| `position-aware-tooltips` | [guides/ui-atoms/position-aware-tooltips.md](guides/ui-atoms/position-aware-tooltips.md) | Build tooltips and popovers with directional arrows (or other visual styling) that automatically point the correct way when the element flips to a fallback position. |
| `pull-to-reveal` | [guides/ui-atoms/pull-to-reveal.md](guides/ui-atoms/pull-to-reveal.md) | Build a pull-to-reveal feature that would enable the user to pull down on the screen to reveal more content, like a search bar. |
| `responsive-table` | [guides/ui-atoms/responsive-table.md](guides/ui-atoms/responsive-table.md) | Build a data table that presents tabular data with proper header semantics, and remains readable and navigable on small screens and with assistive technologies. |
| `scroll-position-aware-elements` | [guides/ui-atoms/scroll-position-aware-elements.md](guides/ui-atoms/scroll-position-aware-elements.md) | Build floating buttons or widgets (back-to-top, scroll-to-bottom, chat launchers, etc.) that appear and disappear based on whether the user has scrolled at all. |
| `scroll-progress-indicator` | [guides/ui-atoms/scroll-progress-indicator.md](guides/ui-atoms/scroll-progress-indicator.md) | Create a scroll progress bar, stepped progress tracker, or any visual affordance that communicates how far through a page or section the user has scrolled. |
| `scrollability-affordance-hints` | [guides/ui-atoms/scrollability-affordance-hints.md](guides/ui-atoms/scrollability-affordance-hints.md) | Build scroll shadows or fading edges that appear only when there's actually more content to scroll to in that direction. |
| `shrinking-header-on-scroll` | [guides/ui-atoms/shrinking-header-on-scroll.md](guides/ui-atoms/shrinking-header-on-scroll.md) | Smoothly animate a fixed header or full-page cover on scroll to dynamically shrink, gain shadows, and transform its layout over a predefined scroll distance. |
| `single-line-overflow` | [guides/ui-atoms/single-line-overflow.md](guides/ui-atoms/single-line-overflow.md) | Show text that must stay on one line, such as a tab label, table cell, navigation item, or file name, in a space it may not fit, without breaking the layout or losing the text. |
| `state-aware-sticky-headers` | [guides/ui-atoms/state-aware-sticky-headers.md](guides/ui-atoms/state-aware-sticky-headers.md) | Build sticky section headers or navbars that visually transform when they're actually "stuck" at the top, changing their color scheme or gaining a shadow. |
| `viewport-aware-dropdowns` | [guides/ui-atoms/viewport-aware-dropdowns.md](guides/ui-atoms/viewport-aware-dropdowns.md) | Position dropdowns, flyouts, or contextual action panels tethered to a trigger button so they automatically flip axes at viewport edges instead of getting clipped. |

## ui-behaviors

| Id | Path | Description |
| --- | --- | --- |
| `2d-panning` | [guides/ui-behaviors/2d-panning.md](guides/ui-behaviors/2d-panning.md) | Allow users to freely pan or scroll two-dimensional surfaces—such as maps, zoomed images, infinite canvases, or large data grids—across both directions (whether diagonally or changing direction mid-gesture) without the gesture locking to a single horizontal or vertical axis. |
| `anchor-positioning-tab-underline` | [guides/ui-behaviors/anchor-positioning-tab-underline.md](guides/ui-behaviors/anchor-positioning-tab-underline.md) | Transition an element seamlessly between two target element positions. |
| `animate-element-entry-exit` | [guides/ui-behaviors/animate-element-entry-exit.md](guides/ui-behaviors/animate-element-entry-exit.md) | Smoothly hide/show elements as they are added/removed from the DOM or as their display values are toggled. |
| `animate-to-from-top-layer` | [guides/ui-behaviors/animate-to-from-top-layer.md](guides/ui-behaviors/animate-to-from-top-layer.md) | Animate elements such as dialogs, popovers, and tooltips as they're entering/exiting the top layer. |
| `carousel-snap-highlights` | [guides/ui-behaviors/carousel-snap-highlights.md](guides/ui-behaviors/carousel-snap-highlights.md) | Visually highlight the currently snapped non-interactive item in scroll-snapping carousels, galleries, or full-page swipe experiences. |
| `consistent-cross-document-transitions` | [guides/ui-behaviors/consistent-cross-document-transitions.md](guides/ui-behaviors/consistent-cross-document-transitions.md) | Ensure critical page state is loaded and stable before initiating a cross-document view transition. |
| `cross-document-transitions` | [guides/ui-behaviors/cross-document-transitions.md](guides/ui-behaviors/cross-document-transitions.md) | Create smooth, seamless transitions between full page navigations, such as cross-fades, custom reveal effects, or morphing of content from one page to the next. |
| `custom-button-actions` | [guides/ui-behaviors/custom-button-actions.md](guides/ui-behaviors/custom-button-actions.md) | Declaratively connect a button to any element to trigger custom, application-specific actions using declarative button commands, invoker commands, button commands, custom commands, or declarative toggle actions. |
| `declarative-dialog-popover-control` | [guides/ui-behaviors/declarative-dialog-popover-control.md](guides/ui-behaviors/declarative-dialog-popover-control.md) | Toggle the visibility of a dialog or popover from a button without writing JavaScript. |
| `directional-navigation-transitions` | [guides/ui-behaviors/directional-navigation-transitions.md](guides/ui-behaviors/directional-navigation-transitions.md) | Animate visual state changes to reflect the direction of a user's navigational flow, such as sliding new content in from the right when advancing forward or from the left when returning to a previous screen. |
| `drag-and-drop` | [guides/ui-behaviors/drag-and-drop.md](guides/ui-behaviors/drag-and-drop.md) | Support dragging to rearrange the children of a container along one axis (horizontal or vertical) while preserving their state and accessible order. |
| `drag` | [guides/ui-behaviors/drag.md](guides/ui-behaviors/drag.md) | Support dragging to move a floating element around the page. |
| `dynamic-sibling-animations` | [guides/ui-behaviors/dynamic-sibling-animations.md](guides/ui-behaviors/dynamic-sibling-animations.md) | Stagger animation or transition timing across sibling elements so each one starts after a computed delay based on its position in the sibling list. |
| `dynamic-sort` | [guides/ui-behaviors/dynamic-sort.md](guides/ui-behaviors/dynamic-sort.md) | Best practices for handling dynamic user-triggered reordering of a container's children (e.g. |
| `group-element-transitions` | [guides/ui-behaviors/group-element-transitions.md](guides/ui-behaviors/group-element-transitions.md) | Smoothly rearrange and animate list items, cards, or grid elements into their new positions simultaneously when adding, removing, shuffling, or reordering—such as removing a product from a shopping cart. |
| `highlight-text-ranges` | [guides/ui-behaviors/highlight-text-ranges.md](guides/ui-behaviors/highlight-text-ranges.md) | Highlight arbitrary text ranges on a page such as search results, spelling errors, or collaborative editing cursors. |
| `interactive-content-reveal` | [guides/ui-behaviors/interactive-content-reveal.md](guides/ui-behaviors/interactive-content-reveal.md) | Create interactive reveal effects, such as a spotlight that follows the user's pointer to uncover details within an image or UI section. |
| `interest-triggered-action-previews` | [guides/ui-behaviors/interest-triggered-action-previews.md](guides/ui-behaviors/interest-triggered-action-previews.md) | Show a live preview of a button's effect when a user signals interest (e.g. |
| `interest-triggered-tooltips` | [guides/ui-behaviors/interest-triggered-tooltips.md](guides/ui-behaviors/interest-triggered-tooltips.md) | Show a tooltip or supplemental information when a user hovers over, focuses on, or long-presses an interactive element, without requiring a click. |
| `light-dismiss-a-dialog` | [guides/ui-behaviors/light-dismiss-a-dialog.md](guides/ui-behaviors/light-dismiss-a-dialog.md) | Create a modal dialog that can be closed via light dismiss (i.e. |
| `motion` | [guides/ui-behaviors/motion.md](guides/ui-behaviors/motion.md) | Animate UI with CSS transitions, animations, scroll-driven animations, and view transitions while keeping motion on the compositor and respecting reduced-motion preferences. |
| `move-dom-element-without-losing-state` | [guides/ui-behaviors/move-dom-element-without-losing-state.md](guides/ui-behaviors/move-dom-element-without-losing-state.md) | Move or reparent a DOM element without losing important element state, such as interactivity states (:focus/:active), `&lt;iframe&gt;` loading state, animation/transition state, etc |
| `parallax-scroll-effects` | [guides/ui-behaviors/parallax-scroll-effects.md](guides/ui-behaviors/parallax-scroll-effects.md) | Create scroll-based effects (such as parallax) where foreground and background layers move at different rates, creating a sense of depth as the user scrolls. |
| `persistent-top-layer-ui` | [guides/ui-behaviors/persistent-top-layer-ui.md](guides/ui-behaviors/persistent-top-layer-ui.md) | Keep a modal dialog, fullscreen element, or native popover visibly open and functionally active when its underlying DOM node is moved or reparented in the DOM. |
| `physics-based-easing` | [guides/ui-behaviors/physics-based-easing.md](guides/ui-behaviors/physics-based-easing.md) | Create custom, physics-based animation and transition effects, like bounce and spring, that feel more natural and engaging than traditional easing curves. |
| `platform-controls-dismiss-dialog` | [guides/ui-behaviors/platform-controls-dismiss-dialog.md](guides/ui-behaviors/platform-controls-dismiss-dialog.md) | Create a modal dialog that can be closed via standard platform-specific user actions, such as pressing the `Esc` key on desktop platforms, or a "back" or "dismiss" gesture on mobile platforms |
| `prevent-page-scroll-under-modal-dialog` | [guides/ui-behaviors/prevent-page-scroll-under-modal-dialog.md](guides/ui-behaviors/prevent-page-scroll-under-modal-dialog.md) | Prevent the underlying page from scrolling while a modal dialog is open. |
| `same-document-transitions` | [guides/ui-behaviors/same-document-transitions.md](guides/ui-behaviors/same-document-transitions.md) | Visually connect persisting elements across different page states or navigations in a Single Page Application (SPA) (e.g. |
| `scoped-component-transitions` | [guides/ui-behaviors/scoped-component-transitions.md](guides/ui-behaviors/scoped-component-transitions.md) | Animate state changes inside a single component (a card, list, panel, or other subtree) while the rest of the page remains interactive, and other transitions run concurrently. |
| `scroll-completion-effects` | [guides/ui-behaviors/scroll-completion-effects.md](guides/ui-behaviors/scroll-completion-effects.md) | Trigger visual effects, animations, or focus changes on a target element only after a smooth programmatic scroll to that element has finished. |
| `scroll-entry-exit-effects` | [guides/ui-behaviors/scroll-entry-exit-effects.md](guides/ui-behaviors/scroll-entry-exit-effects.md) | Create fade-in, scale-up, or other complex reveal-type effects on elements as they enter and exit the scrollport (or viewport) while the user is scrolling. |
| `scroll-snap-realtime-feedback` | [guides/ui-behaviors/scroll-snap-realtime-feedback.md](guides/ui-behaviors/scroll-snap-realtime-feedback.md) | Provide real-time visual feedback in linked UI elements while a user scrolls through snap-aligned content, before the scroll gesture completes. |
| `scroll-snap-state-sync` | [guides/ui-behaviors/scroll-snap-state-sync.md](guides/ui-behaviors/scroll-snap-state-sync.md) | Synchronize navigation indicators, linked content panels, and analytics tracking with the actively snapped item in a scrollable container. |
| `scroll-target-on-load` | [guides/ui-behaviors/scroll-target-on-load.md](guides/ui-behaviors/scroll-target-on-load.md) | Build a scrollable list of elements (e.g. |
| `scrollytelling` | [guides/ui-behaviors/scrollytelling.md](guides/ui-behaviors/scrollytelling.md) | Animate visual properties on a target element — such as fading a backdrop, shifting a background color, or to create scrollytelling experiences — driven entirely by the scrollport position of a completely different element. |
| `search-hidden-content` | [guides/ui-behaviors/search-hidden-content.md](guides/ui-behaviors/search-hidden-content.md) | Hide content from view using patterns such as accordions, tabs, and "Read more" sections, while ensuring the hidden text reveals itself during native "Find in page" searches, allows search engine indexing, supports URL fragment deep links, and maintains ARIA accessibility. |
| `sortable-table` | [guides/ui-behaviors/sortable-table.md](guides/ui-behaviors/sortable-table.md) | Progressively enhance a data table with behaviors that allow users to sort rows by clicking on column headers. |
| `spatial-navigation` | [guides/ui-behaviors/spatial-navigation.md](guides/ui-behaviors/spatial-navigation.md) | Implement accessible spatial navigation using arrow keys that works correctly in different layout modes (grid etc) |
| `swipe-to-remove` | [guides/ui-behaviors/swipe-to-remove.md](guides/ui-behaviors/swipe-to-remove.md) | Let users act on items in a list (remove, archive, mark as read, etc.) with a horizontal swipe gesture, so they can process entries quickly without tapping a separate control. |
| `swipe-to-reveal` | [guides/ui-behaviors/swipe-to-reveal.md](guides/ui-behaviors/swipe-to-reveal.md) | Let users swipe horizontally on a list item or content pane to reveal contextual action buttons or a side menu without automatically triggering an action. |

## ui-components

| Id | Path | Description |
| --- | --- | --- |
| `accordion` | [guides/ui-components/accordion.md](guides/ui-components/accordion.md) | Build an accordion component with animation, optional exclusive (one-open-at-a-time) behavior, and brand-consistent styling. |
| `app-menus` | [guides/ui-components/app-menus.md](guides/ui-components/app-menus.md) | Build an application menu bar where several top-level menus (such as File, Edit, and View) act as a single keyboard stop and switch between each other on hover or arrow keys. |
| `breadcrumbs` | [guides/ui-components/breadcrumbs.md](guides/ui-components/breadcrumbs.md) | Build a breadcrumb trail that shows the user's location within a site hierarchy and lets them navigate to ancestor pages. |
| `card` | [guides/ui-components/card.md](guides/ui-components/card.md) | Build a card component that adapts its presentation to its own available space and contents. |
| `carousel` | [guides/ui-components/carousel.md](guides/ui-components/carousel.md) | Build a carousel component that displays a set of items in a horizontal or vertical layout. |
| `checkbox` | [guides/ui-components/checkbox.md](guides/ui-components/checkbox.md) | Style checkboxes, including custom icons, layout, colors, check/uncheck animations, while preserving native functionality and accessibility. |
| `copy-button` | [guides/ui-components/copy-button.md](guides/ui-components/copy-button.md) | Build a copy button that copies text from arbitrary elements to the clipboard. |
| `dark-mode-toggle` | [guides/ui-components/dark-mode-toggle.md](guides/ui-components/dark-mode-toggle.md) | Build a dark mode toggle component that allows users to override their system color scheme preference for the current site. |
| `dialog` | [guides/ui-components/dialog.md](guides/ui-components/dialog.md) | Build a modal or non-modal dialog component that is accessible, manages focus appropriately, and can be dismissed the way users expect on each platform. |
| `hovercard` | [guides/ui-components/hovercard.md](guides/ui-components/hovercard.md) | Build a hovercard component that displays an interactive structured preview of the page a certain type of link (e.g. |
| `menu` | [guides/ui-components/menu.md](guides/ui-components/menu.md) | Build a menu component that displays a list of options or actions, with support for nested submenus. |
| `navbar` | [guides/ui-components/navbar.md](guides/ui-components/navbar.md) | Build a site navigation bar that adapts across screen sizes and indicates the current page. |
| `navigation-drawer` | [guides/ui-components/navigation-drawer.md](guides/ui-components/navigation-drawer.md) | Create a navigation drawer component that, when triggered from a menu button, slides in from the side overlaid on top of existing page content, and slides out when dismissed (by swiping away, tapping outside, or pressing escape). |
| `persistent-app-tours` | [guides/ui-components/persistent-app-tours.md](guides/ui-components/persistent-app-tours.md) | Create persistent onboarding walkthroughs using tethered native overlays that stay open during user interaction. |
| `persistent-toast-notifications` | [guides/ui-components/persistent-toast-notifications.md](guides/ui-components/persistent-toast-notifications.md) | Create non-intrusive toast and overlay notifications for persistent, stackable messaging and state communication. |
| `progress-ring` | [guides/ui-components/progress-ring.md](guides/ui-components/progress-ring.md) | Build a progress ring component that visually represents the completion status of a task or process, with support for content in the center and brand-consistent styling. |
| `progress` | [guides/ui-components/progress.md](guides/ui-components/progress.md) | Build a styled progress bar that communicates completion of a task or process, in both determinate and indeterminate states. |
| `scrollspy` | [guides/ui-components/scrollspy.md](guides/ui-components/scrollspy.md) | Highlight the currently visible section of a page in a navigation menu |
| `spinner` | [guides/ui-components/spinner.md](guides/ui-components/spinner.md) | Build a loading spinner that communicates busy state to all users, respects reduced-motion preferences, and animates efficiently. |
| `stack-drill-down` | [guides/ui-components/stack-drill-down.md](guides/ui-components/stack-drill-down.md) | Build full-screen hierarchical navigation that lets users drill down into nested views and swipe or navigate back to return, with browser history kept in sync. |
| `tabs` | [guides/ui-components/tabs.md](guides/ui-components/tabs.md) | Build a responsive tabbed interface with good UX when not all tabs fit on screen. |
| `toolbar` | [guides/ui-components/toolbar.md](guides/ui-components/toolbar.md) | Build a toolbar component that displays a set of controls for performing actions. |

## user-experience

| Id | Path | Description |
| --- | --- | --- |
| `content-first-noise-reduction` | [guides/user-experience/content-first-noise-reduction.md](guides/user-experience/content-first-noise-reduction.md) | Maximize content and reduce noise by removing blocking popups, keeping persistent navigation compact, and moving secondary content behind on-demand disclosure. |
| `form-factor-adaptation` | [guides/user-experience/form-factor-adaptation.md](guides/user-experience/form-factor-adaptation.md) | Adapt layouts, controls, and text to any device or container so touch targets stay usable, content fits its space, and nothing collides with system UI. |
| `natural-interactions` | [guides/user-experience/natural-interactions.md](guides/user-experience/natural-interactions.md) | Implement natural interactions with clear hover, focus, and press feedback, motion that opens from its trigger, swipeable content, and keyboard-reachable actions. |

## visual-design

| Id | Path | Description |
| --- | --- | --- |
| `adapt-scrollbar-to-contrast-preferences` | [guides/visual-design/adapt-scrollbar-to-contrast-preferences.md](guides/visual-design/adapt-scrollbar-to-contrast-preferences.md) | Enhance scrollbar visibility for users who prefer high-contrast interfaces |
| `apply-webgl-shaders` | [guides/visual-design/apply-webgl-shaders.md](guides/visual-design/apply-webgl-shaders.md) | Apply custom visual effects with WebGL shaders to HTML content. |
| `browser-ui-theming` | [guides/visual-design/browser-ui-theming.md](guides/visual-design/browser-ui-theming.md) | Theme browser-generated UI such as text selection, scrollbars, form controls, and pickers with CSS instead of re-creating it with custom elements. |
| `color` | [guides/visual-design/color.md](guides/visual-design/color.md) | Color guidance for the web, including contrast requirements, light and dark color schemes, Forced Colors Mode, and generating tints and shades from a base color. |
| `complex-shapes` | [guides/visual-design/complex-shapes.md](guides/visual-design/complex-shapes.md) | Clip elements and their content to any free-form shape, like a symbol, brush stroke, or organic texture for more expressive designs. |
| `contrast-color` | [guides/visual-design/contrast-color.md](guides/visual-design/contrast-color.md) | Select a readable text color with sufficient contrast on a dynamic background color. |
| `custom-text-decorations` | [guides/visual-design/custom-text-decorations.md](guides/visual-design/custom-text-decorations.md) | Add text decorations such as underlines, overlines, strikethroughs, or entirely custom shapes, with reveal animations, custom offsets and end insets, and flexible ink skipping. |
| `customize-scrollbar-color-and-thickness` | [guides/visual-design/customize-scrollbar-color-and-thickness.md](guides/visual-design/customize-scrollbar-color-and-thickness.md) | Customize the color or thickness of a scrollbar |
| `dark-mode` | [guides/visual-design/dark-mode.md](guides/visual-design/dark-mode.md) | Implement dark mode support in a way that respects the user's light/dark theme preference and adapts browser UI (e.g. |
| `equal-width-text-lines` | [guides/visual-design/equal-width-text-lines.md](guides/visual-design/equal-width-text-lines.md) | Make every line of a multi-line heading or lockup span the same width, as in poster-style or stacked-headline typography. |
| `export-html-media-from-canvas` | [guides/visual-design/export-html-media-from-canvas.md](guides/visual-design/export-html-media-from-canvas.md) | Capture and export dynamic HTML content as images or video frames from within canvas. |
| `expose-canvas-content-to-browser-features` | [guides/visual-design/expose-canvas-content-to-browser-features.md](guides/visual-design/expose-canvas-content-to-browser-features.md) | Expose content rendered in a canvas to browser features like assistive technologies, translation, or reading mode. |
| `improve-text-layout-and-legibility` | [guides/visual-design/improve-text-layout-and-legibility.md](guides/visual-design/improve-text-layout-and-legibility.md) | Improve the layout and legibility of short standalone text content, such as headings no longer than a few lines, by enabling the browser to apply evenly balanced line breaks when wrapping text. |
| `interactive-content-in-3d-scenes` | [guides/visual-design/interactive-content-in-3d-scenes.md](guides/visual-design/interactive-content-in-3d-scenes.md) | Integrate interactive HTML elements into a 3D scene. |
| `precise-text-alignment` | [guides/visual-design/precise-text-alignment.md](guides/visual-design/precise-text-alignment.md) | Achieve precise vertical alignment with text of any font. |
| `shaped-cutouts` | [guides/visual-design/shaped-cutouts.md](guides/visual-design/shaped-cutouts.md) | Combine multiple shapes to create complex cutouts or 'knockout' effects in elements, such as adding a notch to an element. |
| `soft-edge-content-fade` | [guides/visual-design/soft-edge-content-fade.md](guides/visual-design/soft-edge-content-fade.md) | Apply a transparency gradient to content edges to indicate further scrollable areas or to obscure payment-walled text. |
| `typography` | [guides/visual-design/typography.md](guides/visual-design/typography.md) | Typography best practices for the web, including font sizing units, line height, text wrapping and balancing, and fluid type that scales with the viewport. |
| `visual-effects` | [guides/visual-design/visual-effects.md](guides/visual-design/visual-effects.md) | Visual effects with CSS such as layered shadows, blend modes, gradients with predictable color interpolation, and patterns like stripes, checkerboards, dots, and pie charts built from gradients alone. |
| `visually-stable-font-fallbacks` | [guides/visual-design/visually-stable-font-fallbacks.md](guides/visual-design/visually-stable-font-fallbacks.md) | Define font styles such that text remains readable and visually consistent in the event that there's a swap between the preferred font and one of the fallbacks (or vice versa). |
| `visually-stable-mixed-fonts` | [guides/visual-design/visually-stable-mixed-fonts.md](guides/visual-design/visually-stable-mixed-fonts.md) | Define font styles such that text remains readable and visually consistent in situations where multiple fonts are used to render a single block of text. |
| `visually-texture-content` | [guides/visual-design/visually-texture-content.md](guides/visual-design/visually-texture-content.md) | Apply realistic weathering and texture patterns to elements to give them an organic, aged, or physical material appearance. |

## wasm

| Id | Path | Description |
| --- | --- | --- |
| `cpp-on-the-web` | [guides/wasm/cpp-on-the-web.md](guides/wasm/cpp-on-the-web.md) | Compile C/C++ to WebAssembly using Emscripten |

## webmcp

| Id | Path | Description |
| --- | --- | --- |
| `agentic-forms` | [guides/webmcp/agentic-forms.md](guides/webmcp/agentic-forms.md) | Expose client-side functionality as tools to AI agents by annotating standard HTML forms with WebMCP attributes. |
| `agentic-javascript-tools` | [guides/webmcp/agentic-javascript-tools.md](guides/webmcp/agentic-javascript-tools.md) | Programmatically register client-side JavaScript functions as tools for AI agents using the WebMCP Imperative API. |
| `webmcp` | [guides/webmcp/webmcp.md](guides/webmcp/webmcp.md) | Use this guide to implement WebMCP in browser applications, exposing client-side functionality as tools to AI agents via declarative or imperative APIs. Early Preview behind a browser flag (upstream wording). |
