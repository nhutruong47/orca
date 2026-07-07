# Knowledge Document: HomePage.tsx (Chunk 6/17)

## Metadata
```json
{
  "file_path": "frontend-web-main/src/pages/HomePage.tsx",
  "language": "tsx",
  "module": "pages",
  "business_domain": "factory",
  "tags": [
    "factory",
    "dashboard",
    "admin",
    "workspace",
    "production",
    "warehouse",
    "inventory",
    "chat"
  ],
  "logical_type": "Component/Page",
  "chunk_index": 5,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
   
    const anim = gsap.to(wheelRef.current, {
      rotation: -360,
      duration: 160,
      ease: 'none',
      repeat: -1,
    });

    const handleMouseEnter = () => anim.pause();
    const handleMouseLeave = () => anim.play();

    const wheelEl = wheelRef.current;
    wheelEl.addEventListener('mouseenter', handleMouseEnter);
    wheelEl.addEventListener('mouseleave', handleMouseLeave);

    return () => {
      wheelEl.removeEventListener('mouseenter', handleMouseEnter);
      wheelEl.removeEventListener('mouseleave', handleMouseLeave);
      anim.kill();
    };
  }, []);

  useEffect(() => {
    document.documentElement.classList.add('luxury-home-page');
    document.body.classList.add('luxury-home-page');

    const animatedItems = Array.from(document.querySelectorAll<HTMLElement>('[data-reveal]'));
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) entry.target.classList.add('is-visible');
        });
      },
      { threshold: 0.18 }
    );

    animatedItems.forEach((item) => observer.observe(item));

    let frame = 0;
    const updateCamera = () => {
      const scrollY = window.scrollY;
      const max = Math.max(window.innerHeight, 1);
      const pageMax = Math.max(document.documentElement.scrollHeight - window.innerHeight, 1);
      const progress = Math.min(scrollY / max, 1);
      const pageProgress = Math.min(scrollY / pageMax, 1);
      setNavScrolled(scrollY > Math.max(window.innerHeight * 0.58, 280));
      setNavHidden(scrollY > 120);
      document.documentElement.style.setProperty('--coffee-hero-y', `${scrollY * 0.18}px`);
      document.documentElement.style.setProperty('--coffee-hero-scale', (1.05 + progress * 0.12).toFixed(3));
      document.documentElement.style.setProperty('--coffee-copy-y', `${scrollY * -0.045}px`);
      document.documentElement.style.setProperty('--coffee-copy-scale', (1 - progress * 0.025).toFixed(3));
      document.documentElement.style.setProperty('--coffee-story-y', `${(pageProgress - 0.18) * -44}px`);
      document.documentElement.style.setProperty('--coffee-story-scale', (1.02 + pageProgress * 0.08).toFixed(3));
      document.documentElement.style.setProperty('--coffee-cinema-scale', (1.04 + pageProgress * 0.045).toFixed(3));
      frame = 0;
    };

    const handleScroll = () => {

```
