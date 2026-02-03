---
name: frontend-design
description: Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code and UI design that avoids generic AI aesthetics.
license: Complete terms in LICENSE.txt
---

This skill guides creation of distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. Implement real working code with exceptional attention to aesthetic details and creative choices.

The user provides frontend requirements: a component, page, application, or interface to build. They may include context about the purpose, audience, or technical constraints.

## 🚀 Quick Start for Beginners

This skill is designed to be beginner-friendly. If you're new to frontend development, just provide:
1. **What you want to build**: e.g., "a landing page for a SaaS product", "a portfolio website", "a dashboard"
2. **Optional - Design reference**: Share any of these:
   - 📸 **Screenshot or image** - Upload or provide path to an image file
   - ✏️ **Hand-drawn sketch** - Photo of your paper sketch or wireframe
   - 🌐 **Website URL** - Link to a site you like the style of (e.g., "make it look like apple.com")
   - 🎨 **Design file** - Figma, Sketch, or other design tool screenshot
3. **Optional - Content**: Your text content, or I'll generate placeholder content for you

**Example usage**:
```
Use the frontend-design skill to create a landing page for my AI startup.
Make it look clean and modern like https://www.stripe.com
```

Or with a screenshot:
```
Use frontend-design to build this page.
[Upload screenshot or provide path: C:\Users\...\design.png]
```

Or with a hand-drawn sketch:
```
I drew a quick sketch of what I want. Use frontend-design to make it real.
[Upload photo of your sketch]
```

If you don't provide details, I'll use smart defaults and ask clarifying questions only when necessary.

## 🛠️ Default Technology Stack

Unless you specify otherwise, projects will use:
- **React 18+** - UI framework
- **Vite 5.x** - Build tool (fast, modern)
- **TypeScript 5.x** - Type safety
- **shadcn/ui** - Beautiful, accessible component library
- **Tailwind CSS 3.x** - Utility-first styling (stable version)
- **Lucide React** - Icon library

**Important Version Notes:**
- **Tailwind CSS**: Using stable 3.x version (NOT 4.x alpha/beta) for production reliability
- All dependencies use stable, well-tested versions
- This stack is production-ready, well-documented, and beginner-friendly

## 📋 Project Types & Defaults

When you ask to build something, I'll automatically configure it based on the type:

### Landing Page (Default)
- Sections: Hero, Features, Testimonials, Pricing, CTA, Footer
- Mobile-responsive with smooth scrolling
- Contact form with validation
- Optimized for conversions

### Portfolio Website
- Sections: About, Projects showcase, Skills, Contact
- Project cards with hover effects
- Responsive image galleries
- Links to GitHub/social media

### Dashboard
- Sidebar navigation
- Data visualization (charts)
- Tables with sorting/filtering
- Responsive layout that works on tablets

### Component Library
- Isolated components with examples
- Interactive demos
- Props documentation
- Copy-paste ready code

### Blog/Content Site
- Article layout with typography
- Category/tag system
- Search functionality
- Reading progress indicator

## 🎯 Beginner-Friendly Workflow

### Step 1: Initial Setup
I'll automatically:
1. Create project structure with `npm create vite@latest`
2. Install and configure Tailwind CSS
3. Set up shadcn/ui with your preferred theme
4. Create a clean folder structure:
   ```
   src/
   ├── components/     # Reusable components
   ├── pages/         # Page components
   ├── lib/           # Utilities
   └── styles/        # Global styles
   ```

### Step 2: Component Generation
I'll build:
- Responsive layouts that work on all devices
- Accessible components (keyboard navigation, screen readers)
- Loading states and error handling
- Smooth animations and transitions

### Step 3: Content Population
If you don't provide content, I'll:
- Generate professional placeholder text
- Use appropriate placeholder images
- Create realistic sample data
- Add helpful comments for easy customization

### Step 4: Polish & Optimization
Automatically included:
- Mobile-first responsive design
- Performance optimization (lazy loading, code splitting)
- SEO-friendly markup
- Accessibility features (ARIA labels, focus states)

## 🎨 Smart Defaults

### Design Tokens
I'll create a cohesive design system with:
- Color palette (primary, secondary, accent, neutrals)
- Typography scale (headings, body, captions)
- Spacing system (4px base grid)
- Border radius, shadows, transitions

### Responsive Breakpoints
- Mobile: < 640px
- Tablet: 640px - 1024px
- Desktop: > 1024px

### Animation Defaults
- Page transitions: 300ms ease-out
- Hover effects: 200ms ease-in-out
- Scroll animations: Intersection Observer with fade-in
- Loading spinners: Smooth, branded animations

## 📦 What You Get

Every project includes:

### 1. Complete Source Code
- Clean, commented TypeScript code
- Reusable components
- Type definitions
- Utility functions

### 2. Styling System
- Tailwind configuration
- CSS variables for theming
- Responsive utility classes
- Dark mode support (optional)

### 3. Component Library
shadcn/ui components pre-configured:
- Button, Input, Card, Dialog
- Dropdown, Tabs, Accordion
- Toast notifications, Form validation
- Data tables, Charts (if needed)

### 4. Documentation
- README with setup instructions
- Component usage examples
- Customization guide
- Deployment instructions

### 5. Development Tools
- ESLint for code quality
- Prettier for formatting
- TypeScript for type checking
- Hot reload for instant feedback

## 🎭 Design Approach Options

Tell me your preferred style, or I'll suggest one based on your project:

### Minimal & Clean
- Lots of white space
- Subtle animations
- Focus on typography
- Examples: Apple, Linear

### Bold & Colorful
- Vibrant gradients
- Strong shadows
- Playful interactions
- Examples: Stripe, Vercel

### Dark & Modern
- Dark background
- Neon accents
- Glassmorphism effects
- Examples: GitHub, Figma

### Corporate & Professional
- Conservative colors
- Structured layouts
- Trust indicators
- Examples: Microsoft, Salesforce

### Creative & Unique
- Custom layouts
- Unexpected interactions
- Artistic typography
- Examples: Awwwards sites

## 🔧 Customization Made Easy

After I build your site, you can easily customize:

### Colors
```typescript
// tailwind.config.js
colors: {
  primary: '#YOUR_COLOR',
  secondary: '#YOUR_COLOR',
}
```

### Content
All text is stored in easy-to-find constants:
```typescript
// src/lib/content.ts
export const HERO_TITLE = "Your Amazing Product"
export const HERO_SUBTITLE = "Built for modern teams"
```

### Components
Each component is self-contained and documented:
```typescript
// src/components/Hero.tsx
interface HeroProps {
  title: string;
  subtitle: string;
  ctaText?: string; // Optional with default
}
```

## 📱 Mobile-First Philosophy

All designs are mobile-first by default:
- Touch-friendly buttons (min 44px)
- Readable text sizes (16px minimum)
- Simplified mobile navigation
- Optimized images for mobile
- Tested on various screen sizes

## ♿ Accessibility Built-In

Every component includes:
- Semantic HTML (header, main, nav, footer)
- ARIA labels for screen readers
- Keyboard navigation support
- Focus indicators
- Sufficient color contrast (WCAG AA)
- Alt text for images

## 🚢 Deployment Ready

Projects come with deployment configurations for:
- **Vercel**: `vercel.json` included
- **Netlify**: `netlify.toml` included
- **GitHub Pages**: Build scripts configured
- **Docker**: Dockerfile for containerization

Simple deployment commands:
```bash
npm run build          # Production build
npm run preview        # Preview production build
vercel deploy         # Deploy to Vercel
```

## 💡 Common Scenarios for Beginners

### 🏢 Business & Professional

#### "I need a landing page fast"
```
Use frontend-design to create a landing page for [your business].
[Optional: Reference URL or screenshot]
```
I'll create:
- Compelling hero section with CTA
- Feature highlights (3-6 features)
- Social proof (testimonials/logos)
- Pricing section (if needed)
- Contact form
- Newsletter signup
- Mobile-responsive layout

#### "I want a company website"
```
Use frontend-design to build a website for my [type] company.
Include: About, Services, Team, Contact
```
I'll create:
- Professional homepage
- Services/Products showcase
- Team member profiles with photos
- Client testimonials
- Contact page with form
- Footer with social links

#### "I need a pricing page"
```
Use frontend-design to create a pricing page with 3 tiers.
[Optional: Reference like Stripe or Notion]
```
I'll create:
- Three-tier pricing cards
- Feature comparison table
- Billing toggle (monthly/yearly)
- FAQ section
- "Get Started" CTAs
- Trust badges

#### "I want to showcase my services"
```
Use frontend-design for a service showcase page.
Services: [list your services]
```
I'll create:
- Service cards with icons
- Detailed service descriptions
- Process/workflow section
- Case studies or examples
- Booking/inquiry form
- Testimonials

### 🎨 Portfolio & Creative

#### "I want to showcase my portfolio"
```
Use frontend-design to build my [designer/developer/photographer] portfolio.
Style: [minimal/bold/creative]
```
I'll build:
- Eye-catching landing page
- Project gallery with filters
- Project detail pages
- About section with bio
- Skills/tools showcase
- Contact form
- Links to social media

#### "I need a photography portfolio"
```
Use frontend-design for a photography portfolio.
[Upload sample photos or reference]
```
I'll create:
- Full-screen image galleries
- Masonry or grid layouts
- Lightbox for image viewing
- Categories/collections
- About the photographer
- Booking inquiry form

#### "I want a resume website"
```
Use frontend-design to turn my resume into a website.
[Paste resume text or upload PDF]
```
I'll create:
- Professional online resume
- Timeline for experience
- Skills visualization
- Education section
- Projects showcase
- Downloadable PDF resume
- Contact information

### 🛍️ E-commerce & Products

#### "I need a product landing page"
```
Use frontend-design for a product landing page.
Product: [your product name]
[Upload product images]
```
I'll create:
- Hero with product image
- Feature highlights
- How it works section
- Pricing and packages
- Customer reviews
- Pre-order or buy button
- FAQ section

#### "I want an online store homepage"
```
Use frontend-design to create an e-commerce homepage.
Store type: [clothing/electronics/etc.]
```
I'll create:
- Featured products slider
- Product categories grid
- Promotional banners
- Best sellers section
- Newsletter signup
- Search bar
- Shopping cart icon

#### "I need a product showcase"
```
Use frontend-design to showcase my products.
[Upload product images]
```
I'll create:
- Product grid with hover effects
- Quick view popups
- Filter and sort options
- Product cards with prices
- "Add to Cart" buttons (UI only)
- Product detail pages

### 📱 Apps & Software

#### "I need a dashboard for my app"
```
Use frontend-design to create a [analytics/admin/user] dashboard.
Data: [what kind of data to show]
```
I'll create:
- Sidebar navigation
- Top bar with user profile
- Chart widgets (line, bar, pie)
- Data tables with search/sort
- Filter dropdowns
- Stats cards (KPIs)
- Responsive layout

#### "I want an app landing page"
```
Use frontend-design for my mobile app landing page.
App: [app name and description]
[Upload app screenshots]
```
I'll create:
- App store badge buttons
- Feature showcase with phone mockups
- How it works section
- User testimonials
- Video demo placeholder
- Download CTA
- Social proof (download numbers)

#### "I need a SaaS product page"
```
Use frontend-design for my SaaS product page.
Reference: [URL like Linear, Notion, etc.]
```
I'll create:
- Clean, modern design
- Product demo section
- Key features grid
- Integration showcase
- Pricing comparison
- Customer logos
- Sign-up form

### 📝 Content & Blogs

#### "I want a blog website"
```
Use frontend-design to create a blog about [topic].
Style: [minimal/magazine/modern]
```
I'll create:
- Blog post grid/list
- Featured post section
- Category filters
- Search functionality
- Author bio card
- Recent posts sidebar
- Newsletter subscription

#### "I need a blog post template"
```
Use frontend-design for a blog post page.
[Paste sample article or reference URL]
```
I'll create:
- Article header with image
- Reading time indicator
- Formatted content (headings, quotes, code)
- Author bio at bottom
- Share buttons
- Related posts
- Comment section placeholder

#### "I want a documentation site"
```
Use frontend-design for documentation pages.
Topics: [list main topics]
```
I'll create:
- Sidebar navigation tree
- Search functionality
- Code syntax highlighting
- Copy code buttons
- Previous/Next navigation
- Table of contents
- Dark/light mode toggle

### 🎓 Education & Learning

#### "I need a course landing page"
```
Use frontend-design for my online course.
Course: [course name]
[Optional: Reference like Udemy]
```
I'll create:
- Course overview hero
- Curriculum/syllabus section
- Instructor bio
- Student testimonials
- Pricing and enrollment CTA
- FAQ section
- Preview video placeholder

#### "I want a school website"
```
Use frontend-design for a [school/training center] website.
Include: Programs, About, Admissions, Contact
```
I'll create:
- Welcoming homepage
- Programs/courses overview
- About/mission section
- Faculty profiles
- Admissions info
- Events calendar
- Contact and location

### 🎉 Events & Booking

#### "I need an event website"
```
Use frontend-design for [event name] website.
Event: [conference/wedding/festival]
Date: [date]
```
I'll create:
- Event details hero
- Schedule/agenda
- Speaker/performer profiles
- Venue information with map
- Ticket/registration form
- Sponsors section
- FAQ

#### "I want a booking page"
```
Use frontend-design for a booking/reservation page.
Service: [restaurant/salon/hotel]
```
I'll create:
- Booking form with date picker
- Service selection
- Time slot picker
- Customer info form
- Confirmation message
- Cancellation policy
- Contact information

### 🏥 Health & Wellness

#### "I need a clinic website"
```
Use frontend-design for a [medical/dental] clinic website.
```
I'll create:
- Clean, trustworthy design
- Services overview
- Doctor/staff profiles
- Appointment booking form
- Insurance information
- Location and hours
- Patient testimonials

#### "I want a fitness website"
```
Use frontend-design for a fitness/gym website.
[Upload gym photos if available]
```
I'll create:
- Energetic, motivating design
- Class schedule
- Membership plans
- Trainer profiles
- Success stories
- Free trial signup
- Facility photos gallery

### 🍔 Food & Restaurant

#### "I need a restaurant website"
```
Use frontend-design for [restaurant name] website.
Cuisine: [type]
[Upload food photos]
```
I'll create:
- Appetizing hero with food imagery
- Menu sections
- Online ordering button (UI)
- Reservation form
- Location and hours
- Photo gallery
- Customer reviews

#### "I want a food delivery app UI"
```
Use frontend-design for a food delivery app interface.
[Sketch or reference]
```
I'll create:
- Restaurant listings
- Food item cards
- Search and filters
- Cart interface
- Checkout flow
- Order tracking (UI)
- User profile page

### 🏠 Real Estate & Local Services

#### "I need a real estate website"
```
Use frontend-design for a real estate listing site.
Property type: [residential/commercial]
```
I'll create:
- Property search with filters
- Property cards with key details
- Property detail pages
- Image galleries
- Agent profiles
- Contact/inquiry forms
- Map integration placeholder

#### "I want a local service website"
```
Use frontend-design for my [plumbing/cleaning/etc.] service.
Service area: [location]
```
I'll create:
- Service area coverage
- Service list with pricing
- Before/after photos
- Customer reviews
- Booking/quote form
- Emergency contact
- License/certification badges

### 🎮 Gaming & Entertainment

#### "I need a game landing page"
```
Use frontend-design for my game [game name].
Genre: [action/puzzle/etc.]
[Upload game screenshots]
```
I'll create:
- Bold, immersive design
- Game trailer placeholder
- Screenshots gallery
- Features/gameplay highlights
- System requirements
- Download/play button
- Community links

### 🤝 Non-Profit & Community

#### "I want a non-profit website"
```
Use frontend-design for [organization name] non-profit.
Cause: [cause description]
```
I'll create:
- Mission statement hero
- Our impact section
- Donation form
- Volunteer signup
- Projects/initiatives
- Success stories
- Transparency (financials)

#### "I need a community forum homepage"
```
Use frontend-design for a community forum.
Topic: [community topic]
```
I'll create:
- Forum categories
- Recent discussions
- Active members showcase
- Join/signup CTA
- Community guidelines
- Search functionality
- Trending topics

### 🛠️ Tools & Utilities

#### "I want a calculator/tool page"
```
Use frontend-design for a [type] calculator tool.
Purpose: [what to calculate]
```
I'll create:
- Input form
- Calculation display
- Result visualization
- How it works section
- Example calculations
- Share results button
- Clear/reset functionality

#### "I need a form builder"
```
Use frontend-design for a multi-step form.
Purpose: [survey/application/quiz]
```
I'll create:
- Progress indicator
- Step-by-step sections
- Input validation
- Back/next buttons
- Summary review
- Success confirmation
- Data display (front-end only)

### 📧 Email & Newsletter

#### "I want a coming soon page"
```
Use frontend-design for a coming soon page.
Product: [what's coming]
Launch: [date]
```
I'll create:
- Countdown timer
- Email capture form
- Brief description
- Social media links
- Teaser image/video
- Notification signup
- FAQ

#### "I need a thank you page"
```
Use frontend-design for a thank you page after [action].
```
I'll create:
- Confirmation message
- Next steps
- Related resources
- Social sharing buttons
- Return to home link
- Customer support info

### 🔧 Developer Tools

#### "I want a developer portfolio"
```
Use frontend-design for my dev portfolio.
Stack: [your tech stack]
[Link to GitHub]
```
I'll create:
- Code-themed design
- Project cards with tech tags
- GitHub integration (UI)
- Blog/articles section
- Skills and tools
- Contact form
- Resume download

#### "I need API documentation"
```
Use frontend-design for API docs.
Endpoints: [list main endpoints]
```
I'll create:
- Sidebar navigation
- Endpoint reference
- Request/response examples
- Authentication guide
- Code snippets
- Try it out section
- Search functionality

### 🎯 Quick Prototypes

#### "I want to prototype an idea"
```
Use frontend-design to prototype [your idea].
[Sketch or rough description]
```
I'll build:
- Core UI mockup
- Interactive elements
- Placeholder data
- Mobile-responsive
- Shareable link
- Fast turnaround (15 min)

#### "I need a wireframe in code"
```
Use frontend-design to turn this wireframe into code.
[Upload wireframe image]
```
I'll create:
- Coded version of wireframe
- Basic styling
- Layout structure
- Ready to be styled further
- Responsive framework
- Component structure

### 🌟 Special Requests

#### "I saw a cool design, can you build it?"
```
Use frontend-design to recreate this design.
[Screenshot or URL]
Make it [your customizations]
```
I'll do:
- Analyze the reference design
- Recreate in modern code
- Add your customizations
- Make it responsive
- Optimize performance

#### "I have multiple pages to build"
```
Use frontend-design to build a multi-page site.
Pages: [list all pages]
[References or descriptions]
```
I'll create:
- All pages with consistent design
- Navigation between pages
- Shared components
- Design system
- Ready to deploy

#### "Can you improve my existing site?"
```
Use frontend-design to improve my site.
Current: [URL or screenshot]
Issues: [what's wrong]
```
I'll deliver:
- Modern redesign
- Fixed issues
- Better performance
- Mobile-responsive
- Cleaner code
- Design improvements

## 🎓 Learning Resources

After I build your project, you can learn more:
- **React**: https://react.dev
- **Vite**: https://vitejs.dev
- **Tailwind CSS**: https://tailwindcss.com
- **shadcn/ui**: https://ui.shadcn.com
- **TypeScript**: https://typescriptlang.org

## 🐛 Common Issues & Solutions

### Styles not applying?
- Check if Tailwind directives are in `src/index.css`
- Verify `tailwind.config.js` content paths
- Ensure you're using Tailwind 3.x (run `npm list tailwindcss`)
- Clear cache: `rm -rf node_modules/.vite`

### Components not found?
- Run `npx shadcn-ui@latest add [component]`
- Check import paths are correct
- Ensure component is exported

### Build errors?
- Run `npm install` to ensure dependencies
- Check TypeScript errors: `npm run type-check`
- Verify Tailwind version is 3.x: `npm list tailwindcss`
- Clear cache and rebuild: `rm -rf dist && npm run build`

### Port already in use?
- Kill the process: `lsof -ti:5173 | xargs kill -9` (Mac/Linux)
- Or use a different port: `npm run dev -- --port 3000`

### Tailwind CSS version mismatch?
- Check current version: `npm list tailwindcss`
- If showing 4.x and you need 3.x: `npm install -D tailwindcss@^3.4.0`
- Clear cache after downgrade: `rm -rf node_modules/.vite && npm run dev`

## 📝 Project Structure Explained

```
my-project/
├── public/              # Static assets (images, fonts)
├── src/
│   ├── components/      # Reusable UI components
│   │   ├── ui/         # shadcn/ui components
│   │   └── layout/     # Layout components (Header, Footer)
│   ├── pages/          # Page components
│   ├── lib/            # Utility functions, constants
│   ├── hooks/          # Custom React hooks
│   ├── styles/         # Global styles, theme
│   ├── App.tsx         # Main app component
│   └── main.tsx        # Entry point
├── package.json        # Dependencies
├── tailwind.config.js  # Tailwind 3.x configuration
├── tsconfig.json       # TypeScript configuration
└── vite.config.ts      # Vite configuration
```

## ⚙️ Tailwind CSS 3.x Configuration

Every project includes a properly configured `tailwind.config.js` for Tailwind 3.x:

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      // Custom colors from design tokens
      colors: {
        primary: {
          DEFAULT: '#635BFF',
          50: '#F5F3FF',
          100: '#EDE9FE',
          200: '#DDD6FE',
          300: '#C4B5FD',
          400: '#A78BFA',
          500: '#635BFF',
          600: '#4F46E5',
          700: '#4338CA',
          800: '#3730A3',
          900: '#312E81',
        },
        // Add more custom colors...
      },

      // Custom font families
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        display: ['Inter Display', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },

      // Custom spacing
      spacing: {
        '128': '32rem',
        '144': '36rem',
      },

      // Custom border radius
      borderRadius: {
        'button': '8px',
        'card': '16px',
      },

      // Custom box shadows
      boxShadow: {
        'primary': '0 4px 12px rgba(99, 91, 255, 0.25)',
        'primary-lg': '0 8px 24px rgba(99, 91, 255, 0.35)',
        'card': '0 2px 8px rgba(0, 0, 0, 0.04)',
        'card-hover': '0 8px 24px rgba(0, 0, 0, 0.08)',
      },

      // Custom animations
      animation: {
        'fade-in': 'fadeIn 0.6s ease-out',
        'slide-up': 'slideUp 0.6s ease-out',
      },

      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [
    // Add Tailwind plugins if needed
    // require('@tailwindcss/forms'),
    // require('@tailwindcss/typography'),
  ],
}
```

**Global CSS (src/index.css):**

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Custom CSS variables for theming */
@layer base {
  :root {
    --color-primary: 99 91 255;
    --color-text: 10 37 64;
    --color-background: 255 255 255;
    --radius: 0.5rem;
  }

  * {
    @apply border-border;
  }

  body {
    @apply bg-background text-text;
    font-feature-settings: "rlig" 1, "calt" 1;
  }
}

/* Custom utility classes */
@layer utilities {
  .text-balance {
    text-wrap: balance;
  }
}
```

**Package.json dependencies (Tailwind 3.x):**

```json
{
  "devDependencies": {
    "tailwindcss": "^3.4.0",
    "postcss": "^8.4.0",
    "autoprefixer": "^10.4.0"
  }
}
```

## 🎯 Advanced Features (Optional)

If you need more advanced features, just ask:
- **Authentication**: Login, signup, password reset
- **Database integration**: Supabase, Firebase, or custom API
- **State management**: Zustand, Redux, or Context
- **Form handling**: React Hook Form with validation
- **Analytics**: Google Analytics, Plausible
- **SEO**: Meta tags, Open Graph, sitemaps
- **Internationalization**: Multi-language support
- **Testing**: Vitest, React Testing Library
- **Animations**: Framer Motion, GSAP
- **3D effects**: Three.js, React Three Fiber

## 🎬 Step-by-Step Build Process

When you use this skill, here's what happens:

### Phase 1: Understanding (1-2 minutes)
I'll quickly understand your needs by analyzing:
- What you want to build
- Any design references you provide
- Your target audience
- Technical requirements

I'll ask clarifying questions ONLY if truly necessary. Otherwise, I'll use smart defaults.

### Phase 2: Project Setup (2-3 minutes)
I'll create your project:
```bash
# Create Vite + React + TypeScript project
npm create vite@latest your-project -- --template react-ts
cd your-project
npm install

# Install Tailwind CSS 3.x (stable version)
npm install -D tailwindcss@^3 postcss autoprefixer
npx tailwindcss init -p

# Install shadcn/ui dependencies
npm install class-variance-authority clsx tailwind-merge
npm install lucide-react

# Install shadcn/ui
npx shadcn-ui@latest init
```

**Version Lock for Stability:**
- Tailwind CSS: `^3.4.0` (latest stable 3.x, NOT 4.x)
- PostCSS: Latest stable
- Autoprefixer: Latest stable

### Phase 3: Building Components (5-10 minutes)
I'll create all your components:
- Layout components (Header, Footer, Sidebar)
- Page sections (Hero, Features, etc.)
- UI components (Button, Card, Input)
- Utility functions and hooks

### Phase 4: Styling & Polish (3-5 minutes)
I'll apply:
- Responsive design (mobile, tablet, desktop)
- Smooth animations and transitions
- Proper spacing and typography
- Color scheme and theming

### Phase 5: Testing & Documentation (2 minutes)
I'll ensure:
- All components work correctly
- Mobile responsiveness
- Accessibility features
- Clear README with instructions

**Total time: ~15-20 minutes for a complete project!**

## 📸 Using Visual References (Screenshots, Sketches, URLs)

This skill can analyze and recreate designs from various visual sources. Here's how to use each type:

### 🌐 Website URL References

**How to use:**
```
Use frontend-design to create a landing page similar to https://www.apple.com
```

**IMPORTANT: For accurate design extraction, I will:**

1. **Use WebFetch to analyze the live URL**
   - Extract actual HTML structure
   - Identify CSS classes and styles
   - Analyze layout patterns
   - Capture responsive breakpoints

2. **Optionally use browser tools (Playwright) to:**
   - Take screenshots of the reference page
   - Inspect computed styles
   - Analyze color values and fonts
   - Measure spacing and dimensions
   - Capture animations and interactions

3. **Extract precise design tokens:**
   - **Colors**: Exact hex codes from CSS
   - **Typography**: Font families, weights, sizes (px/rem)
   - **Spacing**: Margin, padding, gaps (measured in px)
   - **Borders**: Radius, width, style
   - **Shadows**: Box-shadow values
   - **Animations**: Transition timings and easing functions

**What I'll analyze from the URL:**
- ✅ Layout structure and grid system (columns, rows, containers)
- ✅ Typography hierarchy (H1-H6 sizes, line heights, font weights)
- ✅ Exact color palette with hex codes
- ✅ Component styles (buttons, cards, inputs) with precise CSS
- ✅ Animation and transition details
- ✅ Spacing system (margins, paddings, gaps)
- ✅ Responsive breakpoints and mobile layouts
- ✅ SVG icons and image treatments

**What I'll deliver:**
- A React/Vite project with pixel-accurate visual style
- Design tokens matching exact values from the reference
- Similar component library with matching styles
- Recreated layouts matching the reference structure
- Your custom content (or placeholder content)

**For maximum accuracy, you can also:**
```
Use frontend-design to build my portfolio website.
Reference: https://www.linear.app

Also, here are screenshots showing:
[Desktop screenshot]
[Mobile screenshot]
[Specific component details]

Please match these exactly, especially:
- The purple gradient on buttons
- The 16px font size for body text
- The 120px section padding
```

**Example with precise instructions:**
```
Use frontend-design to recreate this design.
URL: https://www.stripe.com/payments

Extract and use:
- Exact colors from their design system
- Same font (they use custom fonts, find similar)
- Matching spacing (measure from screenshots if needed)
- Same button styles and hover effects
- Similar card shadows and borders

I'll also paste a screenshot for accuracy.
[Screenshot]
```

**Analysis Process I'll Follow:**

**Phase 1: URL Inspection**
```
1. Fetch the URL using WebFetch
2. Extract HTML and CSS
3. Identify key design patterns
```

**Phase 2: Visual Verification (if needed)**
```
1. Use Playwright to take screenshots
2. Analyze computed styles from browser
3. Measure exact spacing values
4. Capture color values from rendered page
```

**Phase 3: Design Token Extraction**
```
Example output:
{
  colors: {
    primary: "#635BFF",     // Exact from site
    text: "#0A2540",
    background: "#FFFFFF",
    accent: "#00D4FF"
  },
  typography: {
    heading: "72px/1.1 'Helvetica Neue', sans-serif",
    body: "18px/1.6 'Inter', sans-serif"
  },
  spacing: {
    sectionPadding: "120px",
    elementGap: "48px"
  }
}
```

**Phase 4: Implementation**
```
Create components with exact matching styles
```

**Tips for accurate reference:**
1. **Provide specific page URLs** - Not just homepage, but the exact page you want to reference
2. **Mention key elements** - "Focus on the hero section" or "Match the pricing cards"
3. **Add screenshots** - URLs + screenshots = highest accuracy
4. **Specify measurements** - If you know exact values, share them
5. **Note brand fonts** - Some sites use custom fonts I can't access, I'll find similar alternatives

### 📸 Screenshot/Image References

**How to provide in Claude Code:**
1. **Drag and drop** the image file into the chat window
2. **Copy and paste** the image directly (Ctrl+V / Cmd+V)
3. **Upload** by clicking the attachment button
4. **File path**: Provide path like `C:\Users\YourName\Downloads\design.png`
5. **Share from clipboard**: Take screenshot (Print Screen) and paste

**Claude Code can directly read and analyze:**
- Screenshots you paste
- Images you drag into the chat
- Design files you upload
- Photos of hand-drawn sketches
- Exported design files from Figma/Sketch

**What I'll analyze from screenshots:**
- Layout structure and grid system
- Visual hierarchy (what's emphasized)
- Color scheme and color relationships
- Typography style and hierarchy
- Spacing and padding patterns
- Component shapes (rounded corners, shadows, borders)
- Overall mood and aesthetic
- Image treatment and aspect ratios

**What I'll deliver:**
- Pixel-perfect recreation in code
- Responsive adaptation for mobile/tablet
- Interactive elements (even if static in screenshot)
- All design tokens extracted
- Production-ready React components

**Example usage:**
```
Use frontend-design to build this dashboard.
[Screenshot: dashboard-design.png showing a sidebar with charts and tables]
Make it fully functional with sample data.
```

**Supported image formats:**
- PNG, JPG, JPEG
- WebP
- SVG (for simple designs)
- GIF (will use first frame)

### ✏️ Hand-Drawn Sketch References

**How to provide:**
1. Take a clear photo of your sketch
2. Upload the image
3. Describe any unclear elements

**What I'll interpret from sketches:**
- Layout structure (boxes = sections)
- Content hierarchy (size = importance)
- Component placement
- Navigation structure
- User flow intentions
- Rough spacing proportions

**What I'll add on top of your sketch:**
- Professional design polish
- Color scheme (or you can specify)
- Typography selection
- Proper spacing and alignment
- Component styling
- Animations and interactions
- Responsive design

**Tips for sketching:**
- Use boxes to represent sections/components
- Label key elements ("Header", "CTA Button", "Image Gallery")
- Show hierarchy with size (bigger = more important)
- Indicate relationships with arrows
- Add notes for special requirements
- Don't worry about artistic quality!

**Example usage:**
```
Use frontend-design to build this mobile app interface.
[Photo of napkin sketch showing 3 screens with rough boxes and labels]
It's for a food delivery app. Use bright, appetizing colors.
```

### 🎨 Design File Screenshots (Figma, Sketch, etc.)

**How to provide:**
1. Take a screenshot of your design tool
2. Or export as PNG/JPG from Figma/Sketch
3. Include any design system specs if available

**What I'll extract:**
- Exact colors (if visible in screenshot)
- Font specifications (if labeled)
- Component specifications
- Spacing measurements (if visible)
- Layer structure and organization
- Design system patterns

**Example usage:**
```
Use frontend-design to implement this Figma design.
[Screenshot showing design with visible properties panel]
The design system uses 8px grid spacing.
```

### 🔄 Combining Multiple References

You can mix and match different reference types:

```
Use frontend-design to create an e-commerce product page.
Layout reference: https://www.shopify.com/products
Color scheme: [Screenshot of brand guidelines]
Custom sketch: [Photo of hand-drawn custom features]
Content: See attached product descriptions
```

### 🎯 What Happens During Analysis

**Phase 1: Visual Analysis (30 seconds)**
I'll examine the reference and identify:
- Primary design elements
- Color palette extraction
- Typography patterns
- Component inventory
- Layout grid system
- Interaction patterns

**Phase 2: Design System Creation (1 minute)**
I'll create a matching design system:
- Color tokens
- Typography scale
- Spacing system
- Component variants
- Animation timings

**Phase 3: Implementation (10-15 minutes)**
I'll build the project:
- Component structure
- Responsive layouts
- Interactive elements
- Sample data/content
- Polished animations

**Phase 4: Refinement**
I'll add finishing touches:
- Accessibility features
- Performance optimization
- Mobile responsiveness
- Cross-browser compatibility

### 📋 Reference Analysis Output

After analyzing your reference, I'll provide:

```
✅ Reference Analysis Complete:

Design Style: Minimal, clean, modern
Color Palette:
  - Primary: #0070f3 (Blue)
  - Secondary: #ff0080 (Pink)
  - Background: #ffffff (White)
  - Text: #000000 (Black)
  - Accent: #7928ca (Purple)

Typography:
  - Display: Inter Bold, 48px
  - Heading: Inter SemiBold, 32px
  - Body: Inter Regular, 16px
  - Small: Inter Regular, 14px

Layout:
  - Max width: 1200px
  - Grid: 12 columns
  - Gutter: 24px
  - Section padding: 120px vertical

Components Identified:
  - Hero with gradient background
  - Feature cards (3-column grid)
  - Testimonial carousel
  - Newsletter signup form
  - Footer with social links

Now building your project...
```

### 🚨 Reference Quality Tips

**For best results:**

✅ **Good references:**
- Clear, high-resolution images
- Full page screenshots (not cropped)
- Multiple views if available (desktop + mobile)
- Visible design elements (not blurred)
- Labeled sketches

❌ **Poor references:**
- Blurry or low-resolution images
- Heavily cropped screenshots
- Only partial views
- Extreme angles (for photos)
- Multiple unrelated styles

### 💡 Pro Tips for Visual References

1. **For URLs**: Provide the exact page URL, not just the homepage
2. **For Screenshots**: Include both desktop and mobile views if possible
3. **For Sketches**: Add color notes or mood board images
4. **For Design Files**: Export at 2x resolution for clarity
5. **Multiple References**: Specify which aspects to take from each

### 🎨 Style Mixing Examples

**Example 1: URL + Custom Colors**
```
Use frontend-design to build a landing page.
Layout: https://www.stripe.com/payments
Colors: Use my brand colors #2D3748 (dark blue) and #48BB78 (green)
```

**Example 2: Screenshot + Additional Features**
```
Use frontend-design to recreate this design.
[Screenshot of competitor's homepage]
Add: Animated statistics counter, chatbot widget, dark mode toggle
```

**Example 3: Sketch + Professional Polish**
```
Here's my rough sketch for a booking app.
[Photo of sketch]
Make it professional with: modern fonts, soft shadows, smooth animations
```

## 📖 Usage Examples for Beginners

### Example 1: Simple Landing Page
**Your request:**
```
Use frontend-design to create a landing page for my coffee shop website.
Include sections: home, menu, about us, contact.
```

**What I'll build:**
- Modern, warm design with coffee theme
- Hero section with call-to-action button
- Menu showcase with images
- About section with story
- Contact form with map
- Mobile-responsive layout

### Example 1.5: Using a Screenshot Reference
**Your request:**
```
Use frontend-design to build a landing page like this.
[Paste screenshot of https://www.bluebottle.com]
It's for my coffee subscription service.
```

**What I'll do:**
1. Analyze the screenshot layout and design
2. Extract colors, fonts, spacing
3. Identify component patterns
4. Recreate in React + Tailwind
5. Adapt for your coffee subscription content

**What I'll build:**
- Similar visual style and layout structure
- Matching color palette and typography
- Your custom content about coffee subscriptions
- Mobile-responsive adaptation
- Interactive elements (carousels, forms)

### Example 2: Portfolio Website
**Your request:**
```
Use frontend-design to build my personal portfolio.
I'm a graphic designer. Make it creative and bold.
```

**What I'll build:**
- Creative, visual-heavy design
- Animated hero with your name
- Project gallery with hover effects
- About section with photo
- Skills section with progress bars
- Contact form
- Links to social media

### Example 3: SaaS Landing Page
**Your request:**
```
Use frontend-design for my project management tool landing page.
Reference: https://www.notion.so (similar clean style)
```

**What I'll build:**
- Clean, minimal design inspired by Notion
- Hero with product screenshot
- Feature comparison table
- Pricing tiers
- Testimonials slider
- FAQ accordion
- Sign-up form

### Example 4: Dashboard
**Your request:**
```
Use frontend-design to create an analytics dashboard.
I need charts, tables, and filters.
```

**What I'll build:**
- Sidebar navigation
- Top bar with user profile
- Chart widgets (line, bar, pie)
- Data table with search/sort
- Filter dropdowns
- Responsive grid layout

### Example 5: Using a Hand-Drawn Sketch
**Your request:**
```
Use frontend-design to build this app I sketched.
[Photo of napkin sketch showing:
- Top bar with logo and search
- Left sidebar with menu items
- Main area with card grid
- Bottom navigation on mobile]
It's a recipe discovery app. Make it colorful and fun!
```

**What I'll do:**
1. Interpret your layout structure from the sketch
2. Identify sections: header, sidebar, content area
3. Choose vibrant, food-friendly colors
4. Design professional card components
5. Add search functionality UI
6. Create responsive mobile layout

**What I'll build:**
- Professional UI based on your sketch layout
- Colorful, appetizing design theme
- Recipe cards with images and ratings
- Functional search bar
- Responsive sidebar (hamburger menu on mobile)
- Sample recipe data
- Smooth animations and hover effects

### Example 6: Combining Screenshot + Customization
**Your request:**
```
Use frontend-design to build a pricing page.
Layout reference: [Screenshot of Stripe's pricing page]
But use these brand colors: #6366F1 (indigo), #10B981 (green)
And add a "Compare Plans" table at the bottom
```

**What I'll do:**
1. Analyze Stripe's pricing layout structure
2. Extract their component patterns
3. Replace colors with your brand colors
4. Add custom comparison table
5. Maintain the clean, professional feel

**What I'll build:**
- Stripe-style pricing cards with your colors
- Three-tier pricing structure
- Feature checkmarks and highlights
- Custom comparison table
- Mobile-responsive layout
- "Get Started" CTAs

## 🎨 Design Token System

Every project includes a consistent design system you can easily customize:

### Color Tokens
```typescript
// src/lib/design-tokens.ts
export const colors = {
  // Brand colors
  primary: {
    50: '#eff6ff',
    100: '#dbeafe',
    500: '#3b82f6', // Main brand color
    600: '#2563eb',
    900: '#1e3a8a',
  },

  // Neutral colors
  gray: {
    50: '#f9fafb',
    100: '#f3f4f6',
    500: '#6b7280',
    900: '#111827',
  },

  // Semantic colors
  success: '#10b981',
  warning: '#f59e0b',
  error: '#ef4444',
  info: '#3b82f6',
}
```

### Typography Tokens
```typescript
export const typography = {
  // Font families
  fontFamily: {
    sans: ['Inter', 'sans-serif'],
    display: ['Cal Sans', 'sans-serif'],
    mono: ['JetBrains Mono', 'monospace'],
  },

  // Font sizes
  fontSize: {
    xs: '0.75rem',    // 12px
    sm: '0.875rem',   // 14px
    base: '1rem',     // 16px
    lg: '1.125rem',   // 18px
    xl: '1.25rem',    // 20px
    '2xl': '1.5rem',  // 24px
    '3xl': '1.875rem', // 30px
    '4xl': '2.25rem',  // 36px
  },

  // Font weights
  fontWeight: {
    normal: 400,
    medium: 500,
    semibold: 600,
    bold: 700,
  },
}
```

### Spacing Tokens
```typescript
export const spacing = {
  // 4px base unit
  0: '0',
  1: '0.25rem',  // 4px
  2: '0.5rem',   // 8px
  3: '0.75rem',  // 12px
  4: '1rem',     // 16px
  6: '1.5rem',   // 24px
  8: '2rem',     // 32px
  12: '3rem',    // 48px
  16: '4rem',    // 64px
  24: '6rem',    // 96px
}
```

### Animation Tokens
```typescript
export const animation = {
  // Timing functions
  ease: {
    in: 'cubic-bezier(0.4, 0, 1, 1)',
    out: 'cubic-bezier(0, 0, 0.2, 1)',
    inOut: 'cubic-bezier(0.4, 0, 0.2, 1)',
  },

  // Durations
  duration: {
    fast: '150ms',
    normal: '300ms',
    slow: '500ms',
  },
}
```

## 🧩 Component Templates

Here are the standard components I'll create for you:

### Button Component
```typescript
// src/components/ui/Button.tsx
interface ButtonProps {
  children: React.ReactNode;
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  onClick?: () => void;
  disabled?: boolean;
}

export function Button({
  children,
  variant = 'primary',
  size = 'md',
  ...props
}: ButtonProps) {
  return (
    <button
      className={cn(
        'rounded-lg font-medium transition-all',
        'hover:scale-105 active:scale-95',
        {
          'bg-blue-600 text-white hover:bg-blue-700': variant === 'primary',
          'bg-gray-200 text-gray-900 hover:bg-gray-300': variant === 'secondary',
          'bg-transparent hover:bg-gray-100': variant === 'ghost',
          'px-3 py-1.5 text-sm': size === 'sm',
          'px-4 py-2 text-base': size === 'md',
          'px-6 py-3 text-lg': size === 'lg',
        }
      )}
      {...props}
    >
      {children}
    </button>
  );
}
```

### Card Component
```typescript
// src/components/ui/Card.tsx
interface CardProps {
  children: React.ReactNode;
  className?: string;
  hover?: boolean;
}

export function Card({ children, className, hover = false }: CardProps) {
  return (
    <div
      className={cn(
        'rounded-xl border border-gray-200 bg-white p-6 shadow-sm',
        hover && 'transition-shadow hover:shadow-lg',
        className
      )}
    >
      {children}
    </div>
  );
}
```

### Input Component
```typescript
// src/components/ui/Input.tsx
interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
}

export function Input({ label, error, className, ...props }: InputProps) {
  return (
    <div className="space-y-1">
      {label && (
        <label className="text-sm font-medium text-gray-700">
          {label}
        </label>
      )}
      <input
        className={cn(
          'w-full rounded-lg border border-gray-300 px-4 py-2',
          'focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200',
          error && 'border-red-500',
          className
        )}
        {...props}
      />
      {error && (
        <p className="text-sm text-red-600">{error}</p>
      )}
    </div>
  );
}
```

## 🎯 Layout Patterns

### Full-Width Hero
```typescript
function Hero() {
  return (
    <section className="relative min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="container mx-auto px-4">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-6xl font-bold text-gray-900 mb-6">
            Build Amazing Products
          </h1>
          <p className="text-xl text-gray-600 mb-8">
            The fastest way to ship your ideas to production
          </p>
          <div className="flex gap-4 justify-center">
            <Button size="lg">Get Started</Button>
            <Button variant="secondary" size="lg">Learn More</Button>
          </div>
        </div>
      </div>
    </section>
  );
}
```

### Feature Grid
```typescript
function Features() {
  const features = [
    {
      icon: Zap,
      title: 'Lightning Fast',
      description: 'Built with performance in mind from day one',
    },
    {
      icon: Shield,
      title: 'Secure by Default',
      description: 'Enterprise-grade security out of the box',
    },
    {
      icon: Sparkles,
      title: 'Beautiful UI',
      description: 'Polished components that users love',
    },
  ];

  return (
    <section className="py-24 bg-white">
      <div className="container mx-auto px-4">
        <h2 className="text-4xl font-bold text-center mb-16">
          Everything You Need
        </h2>
        <div className="grid md:grid-cols-3 gap-8">
          {features.map((feature) => (
            <Card key={feature.title} hover>
              <feature.icon className="w-12 h-12 text-blue-600 mb-4" />
              <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
              <p className="text-gray-600">{feature.description}</p>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}
```

### Contact Form
```typescript
function ContactForm() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: '',
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Handle form submission
    console.log('Form submitted:', formData);
  };

  return (
    <section className="py-24 bg-gray-50">
      <div className="container mx-auto px-4">
        <div className="max-w-2xl mx-auto">
          <h2 className="text-4xl font-bold text-center mb-12">
            Get in Touch
          </h2>
          <Card>
            <form onSubmit={handleSubmit} className="space-y-6">
              <Input
                label="Name"
                placeholder="John Doe"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              />
              <Input
                label="Email"
                type="email"
                placeholder="john@example.com"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              />
              <div className="space-y-1">
                <label className="text-sm font-medium text-gray-700">
                  Message
                </label>
                <textarea
                  className="w-full rounded-lg border border-gray-300 px-4 py-2 h-32 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
                  placeholder="Your message..."
                  value={formData.message}
                  onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                />
              </div>
              <Button type="submit" size="lg" className="w-full">
                Send Message
              </Button>
            </form>
          </Card>
        </div>
      </div>
    </section>
  );
}
```

## 🔥 Best Practices for Beginners

### 1. Component Organization
- Keep components small and focused (one responsibility)
- Use descriptive names (e.g., `ProductCard` not `Card2`)
- Group related components in folders
- Export components from index files

### 2. Styling Consistency
- Use Tailwind utility classes
- Create reusable CSS variables for colors
- Follow the design token system
- Use `cn()` utility for conditional classes

### 3. TypeScript Tips
- Define interfaces for all props
- Use optional props with default values
- Export types for reusability
- Enable strict mode in `tsconfig.json`

### 4. Performance Optimization
- Use `React.memo()` for expensive components
- Implement lazy loading for routes
- Optimize images (use WebP format)
- Code-split large components

### 5. Accessibility
- Use semantic HTML elements
- Add `aria-label` for icon buttons
- Ensure keyboard navigation works
- Test with screen readers

## 🚀 Quick Commands Reference

```bash
# Development
npm run dev              # Start dev server (http://localhost:5173)
npm run build           # Build for production
npm run preview         # Preview production build

# Component Management (shadcn/ui)
npx shadcn-ui@latest add button    # Add button component
npx shadcn-ui@latest add card      # Add card component
npx shadcn-ui@latest add input     # Add input component
npx shadcn-ui@latest add dialog    # Add dialog component

# Tailwind CSS 3.x
npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch

# Version Check (ensure Tailwind 3.x)
npm list tailwindcss    # Should show 3.x.x, not 4.x

# Type Checking
npm run type-check      # Check TypeScript errors

# Linting
npm run lint           # Run ESLint
npm run lint:fix       # Auto-fix linting issues

# Formatting
npm run format         # Format code with Prettier

# Dependency Management
npm install -D tailwindcss@^3   # Ensure Tailwind 3.x if upgrading
npm outdated                     # Check for updates (don't upgrade to Tailwind 4.x)
```

## 📱 Responsive Design Helpers

### Mobile-First Breakpoints
```typescript
// Use Tailwind responsive prefixes
<div className="
  text-base           {/* Mobile (default) */}
  sm:text-lg          {/* Tablet (640px+) */}
  md:text-xl          {/* Desktop (768px+) */}
  lg:text-2xl         {/* Large Desktop (1024px+) */}
  xl:text-3xl         {/* Extra Large (1280px+) */}
">
  Responsive Text
</div>
```

### Container Widths
```typescript
<div className="
  container           {/* Centers and constrains width */}
  mx-auto            {/* Centers horizontally */}
  px-4               {/* Padding on mobile */}
  sm:px-6            {/* More padding on tablet */}
  lg:px-8            {/* More padding on desktop */}
">
  Content
</div>
```

### Grid Layouts
```typescript
<div className="
  grid               {/* CSS Grid */}
  grid-cols-1        {/* 1 column on mobile */}
  sm:grid-cols-2     {/* 2 columns on tablet */}
  lg:grid-cols-3     {/* 3 columns on desktop */}
  gap-4              {/* Space between items */}
">
  {items.map(item => <Card key={item.id} />)}
</div>
```

## 🎓 Next Steps After Your Project

Once I've built your project, you can:

1. **Customize Content**: Edit text, images, colors in the code
2. **Add Features**: Request additional functionality
3. **Deploy**: Push to Vercel, Netlify, or GitHub Pages
4. **Learn**: Study the code to understand how it works
5. **Expand**: Add authentication, database, API integration

## 💬 Common Questions

**Q: Do I need to know React to use this?**
A: No! I'll build everything for you. The code is well-commented so you can learn as you go.

**Q: Can I use a different design than you suggest?**
A: Absolutely! Just share a reference website or describe the style you want.

**Q: How do I share a screenshot or sketch?**
A: Simply drag and drop the image into Claude Code, paste it (Ctrl+V), or provide the file path. I can read PNG, JPG, WebP, and other image formats.

**Q: Can you recreate a design from a website URL?**
A: Yes! Just share the URL and I'll analyze the design, extract colors/fonts/layout, and recreate it in React code.

**Q: What if my sketch is rough or messy?**
A: That's perfect! I can interpret rough sketches. Just label the main sections (like "Header", "Menu", "CTA") and I'll turn it into a professional design.

**Q: Can you match an exact design from a screenshot?**
A: Yes! I'll analyze the screenshot and recreate it pixel-perfect in code, making it responsive and interactive.

**Q: What if the reference website needs authentication to view?**
A: Take a screenshot of the logged-in view and paste it. I can work from screenshots of any interface.

**Q: Can I combine multiple references?**
A: Absolutely! You can mix references: "Use layout from [URL], colors from [Screenshot], and add features from [Sketch]"

**Q: Will it work on mobile devices?**
A: Yes! All projects are mobile-responsive by default, even if the reference is desktop-only.

**Q: Can I add my own content later?**
A: Yes! The code is organized to make it easy to find and edit content.

**Q: Do I need to install anything?**
A: Just Node.js (v16+) and npm. I'll guide you through the rest.

**Q: Can you add a backend/database?**
A: Yes! Just ask for features like "add user authentication" or "connect to a database".

**Q: How much does this cost?**
A: The tools are free and open-source. Hosting on Vercel/Netlify is also free for small projects.

**Q: What if I only have a Figma link?**
A: If you can't share the Figma file directly, take screenshots of your designs (including the properties panel if possible) and paste them.

**Q: Can you improve my existing website?**
A: Yes! Share a screenshot of your current site and tell me what you want to improve. I'll rebuild it with modern code and better design.

**Q: Which version of Tailwind CSS do you use?**
A: I use **Tailwind CSS 3.x** (latest stable version like 3.4.x). I do NOT use Tailwind 4.x as it may still be in alpha/beta. This ensures production stability and compatibility with all tooling.

**Q: Can I use Tailwind CSS 4 instead?**
A: Yes, if you specifically request it. But I recommend sticking with Tailwind 3.x for production projects due to its stability and extensive ecosystem support.

**Q: How do I check my Tailwind version?**
A: Run `npm list tailwindcss` in your project directory. You should see version 3.x.x (e.g., 3.4.1).

## 🎯 Ensuring Design Accuracy (CRITICAL)

When using URL or screenshot references, follow these strict guidelines for accuracy:

### Step 1: Reference Analysis (MANDATORY)

**For URL References:**
```typescript
// I MUST use these tools in order:
1. WebFetch - Fetch the URL and extract HTML/CSS
2. Playwright (if available) - Take screenshots and inspect styles
3. Read tool - If user provides local screenshots
```

**Analysis Checklist:**
- [ ] Extract exact color values (hex codes, not approximations)
- [ ] Identify actual font families used (check CSS, find similar if custom)
- [ ] Measure spacing values (px, rem, em from computed styles)
- [ ] Capture button styles (padding, border-radius, box-shadow)
- [ ] Note animation timings and easing functions
- [ ] Document responsive breakpoints
- [ ] List all component variations (button states, card types)

### Step 2: Design Token Extraction (MANDATORY)

**I MUST create a design-tokens.ts file with extracted values:**

```typescript
// design-tokens.ts - Extracted from reference
export const designTokens = {
  // EXACT colors from reference (not guessed)
  colors: {
    primary: "#635BFF",        // From btn-primary class
    primaryHover: "#4F46E5",   // From :hover state
    text: "#0A2540",           // From body text
    textMuted: "#425466",      // From secondary text
    background: "#FFFFFF",     // From body background
    surface: "#F6F9FC",        // From card background
    border: "#E3E8EE",         // From dividers
    success: "#00D4FF",        // From success states
    error: "#DF1B41",          // From error states
  },

  // EXACT typography from reference
  typography: {
    fontFamily: {
      // Primary font from site (or similar alternative)
      sans: "'Inter', -apple-system, sans-serif",
      // Display font if different
      display: "'Inter Display', sans-serif",
      // Monospace if used
      mono: "'Roboto Mono', monospace",
    },
    fontSize: {
      // Measured from computed styles
      xs: "12px",
      sm: "14px",
      base: "16px",    // Base body text size
      lg: "18px",
      xl: "20px",
      "2xl": "24px",
      "3xl": "30px",
      "4xl": "36px",
      "5xl": "48px",
      "6xl": "60px",   // Hero heading size
    },
    fontWeight: {
      normal: 400,
      medium: 500,
      semibold: 600,
      bold: 700,
    },
    lineHeight: {
      tight: 1.1,      // For headings
      normal: 1.5,     // For body
      relaxed: 1.75,   // For long-form content
    },
  },

  // EXACT spacing from reference
  spacing: {
    // Section padding
    sectionY: "120px",        // Vertical section padding (desktop)
    sectionYMobile: "60px",   // Vertical section padding (mobile)
    sectionX: "24px",         // Horizontal container padding

    // Element spacing
    elementGap: "48px",       // Gap between major elements
    cardGap: "24px",          // Gap between cards
    textGap: "16px",          // Gap between text elements

    // Container
    containerMaxWidth: "1280px",
    contentMaxWidth: "768px", // For text content
  },

  // EXACT component styles
  components: {
    button: {
      // Primary button from reference
      primary: {
        padding: "12px 24px",
        fontSize: "16px",
        fontWeight: 600,
        borderRadius: "8px",
        background: "linear-gradient(135deg, #635BFF 0%, #4F46E5 100%)",
        boxShadow: "0 4px 12px rgba(99, 91, 255, 0.25)",
        transition: "all 0.2s ease",
        hoverTransform: "translateY(-2px)",
        hoverShadow: "0 8px 24px rgba(99, 91, 255, 0.35)",
      },
      secondary: {
        padding: "12px 24px",
        fontSize: "16px",
        fontWeight: 600,
        borderRadius: "8px",
        background: "transparent",
        border: "2px solid #E3E8EE",
        color: "#0A2540",
        transition: "all 0.2s ease",
      },
    },
    card: {
      padding: "32px",
      borderRadius: "16px",
      background: "#FFFFFF",
      border: "1px solid #E3E8EE",
      boxShadow: "0 2px 8px rgba(0, 0, 0, 0.04)",
      hoverShadow: "0 8px 24px rgba(0, 0, 0, 0.08)",
      transition: "all 0.3s ease",
    },
    input: {
      padding: "12px 16px",
      fontSize: "16px",
      borderRadius: "8px",
      border: "1px solid #E3E8EE",
      focusBorder: "2px solid #635BFF",
      focusRing: "0 0 0 3px rgba(99, 91, 255, 0.1)",
    },
  },

  // EXACT animations from reference
  animations: {
    // Transition timings
    fast: "150ms",
    normal: "200ms",
    slow: "300ms",

    // Easing functions (check from CSS)
    easeOut: "cubic-bezier(0, 0, 0.2, 1)",
    easeInOut: "cubic-bezier(0.4, 0, 0.2, 1)",

    // Specific animations
    fadeIn: {
      duration: "600ms",
      easing: "cubic-bezier(0, 0, 0.2, 1)",
      delay: "0ms",
    },
    slideUp: {
      duration: "600ms",
      easing: "cubic-bezier(0, 0, 0.2, 1)",
      transform: "translateY(20px) to translateY(0)",
    },
  },

  // EXACT breakpoints from reference
  breakpoints: {
    sm: "640px",
    md: "768px",
    lg: "1024px",
    xl: "1280px",
    "2xl": "1536px",
  },
};
```

### Step 3: Verification Steps (MANDATORY)

Before delivering the project, I MUST verify:

**Visual Accuracy Checklist:**
- [ ] Colors match exactly (use extracted hex codes)
- [ ] Font sizes match (compare with reference)
- [ ] Spacing matches (measure against reference)
- [ ] Button styles match (size, padding, shadows)
- [ ] Card styles match (borders, shadows, radius)
- [ ] Layout structure matches (grid, flexbox, alignment)
- [ ] Responsive behavior matches (test mobile view)
- [ ] Animations match (timing, easing, effects)

**Code Quality Checklist:**
- [ ] Design tokens file created and used throughout
- [ ] Components use token values (not hardcoded)
- [ ] Tailwind config extended with custom values
- [ ] CSS variables defined for dynamic theming
- [ ] No magic numbers in code (all values from tokens)

### Step 4: Reporting Accuracy

**When delivering, I MUST include:**

```markdown
## Design Analysis Report

### Reference: [URL or screenshot]

### Extracted Design Tokens:
- **Primary Color**: #635BFF (from .btn-primary)
- **Text Color**: #0A2540 (from body)
- **Heading Font**: Inter Display, 60px, Bold
- **Body Font**: Inter, 16px, Regular
- **Section Padding**: 120px vertical, 24px horizontal
- **Button Radius**: 8px
- **Card Shadow**: 0 2px 8px rgba(0,0,0,0.04)

### Component Accuracy:
✅ Hero section - 98% match (slight font weight difference)
✅ Feature cards - 100% match
✅ Buttons - 100% match (colors, padding, shadows)
✅ Typography - 95% match (using Inter instead of custom font)
✅ Spacing - 100% match
✅ Colors - 100% match (extracted exact values)

### Notes:
- Reference uses custom font "Stripe UI", replaced with Inter
- Animations approximate (exact timing not visible in static page)
- All major visual elements matched exactly
```

### Step 5: Implementation Standards

**When coding, I MUST:**

1. **Use extracted tokens everywhere:**
```tsx
// ❌ BAD - Hardcoded values
<button className="bg-blue-600 px-6 py-3 rounded-lg">

// ✅ GOOD - Using design tokens
<button className="bg-primary px-6 py-3 rounded-button">
```

2. **Match exact component styles:**
```tsx
// Button must match reference exactly
<Button
  className="px-6 py-3 text-base font-semibold rounded-lg
             bg-gradient-to-r from-primary to-primary-dark
             shadow-primary hover:shadow-primary-lg
             transition-all duration-200 ease-out
             hover:-translate-y-0.5"
>
  Get Started
</Button>
```

3. **Use proper spacing:**
```tsx
// Section spacing from tokens
<section className="py-30 px-6 md:py-40">  {/* 120px = py-30 on Tailwind */}
  <div className="max-w-7xl mx-auto">      {/* 1280px max width */}
    <div className="space-y-12">           {/* 48px gap */}
```

4. **Match typography exactly:**
```tsx
<h1 className="text-6xl font-bold leading-tight">  {/* 60px, bold, 1.1 line-height */}
<p className="text-base leading-normal text-text-muted">  {/* 16px, 1.5 line-height */}
```

### Tools I Will Use for Accuracy:

1. **WebFetch** - Fetch and analyze URL HTML/CSS
2. **Playwright** - Take screenshots and inspect computed styles
3. **Read** - Analyze user-provided screenshots
4. **Color extraction** - Get exact hex codes from rendered elements
5. **Font detection** - Identify font families and find alternatives
6. **Spacing measurement** - Calculate exact padding/margin values

### Font Matching Guidelines:

If reference uses custom/premium fonts I can't access:

**Custom Font → Alternative Mapping:**
- Stripe UI → Inter
- Graphik → Inter
- GT America → Inter or Manrope
- Söhne → Inter or IBM Plex Sans
- Calibre → Inter or Open Sans
- Untitled Sans → Inter or Space Grotesk
- Custom Serif → Merriweather or Lora
- SF Pro → -apple-system or Inter

**I MUST document font substitutions in the delivery report.**

## Design Thinking

Before coding, understand the context and commit to a BOLD aesthetic direction:
- **Purpose**: What problem does this interface solve? Who uses it?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc. There are so many flavors to choose from. Use these for inspiration but design one that is true to the aesthetic direction.
- **Constraints**: Technical requirements (framework, performance, accessibility).
- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.

**WHEN USING REFERENCES**: Follow the "Ensuring Design Accuracy" guidelines above. Extract exact design tokens, verify accuracy, and report deviations.

Then implement working code (HTML/CSS/JS, React, Vue, etc.) that is:
- Production-grade and functional
- Visually striking and memorable (or accurately matching reference)
- Cohesive with a clear aesthetic point-of-view
- Meticulously refined in every detail

## Frontend Aesthetics Guidelines

Focus on:
- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.
- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.
- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Use Motion library for React when available. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.
- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.
- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.

NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.

Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices (Space Grotesk, for example) across generations.

**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.

Remember: Claude is capable of extraordinary creative work. Don't hold back, show what can truly be created when thinking outside the box and committing fully to a distinctive vision.
