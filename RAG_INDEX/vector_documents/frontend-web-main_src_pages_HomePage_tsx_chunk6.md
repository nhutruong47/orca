# Knowledge Document: HomePage.tsx (Chunk 7/17)

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
  "chunk_index": 6,
  "total_chunks": 17
}
```

## Semantic Context
- **Purpose**: Implementation chunk of Component/Page in pages.
- **Dependencies**: Refer to module imports.
- **Tags**: factory, dashboard, admin, workspace, production, warehouse, inventory, chat

## Source Code Chunk
```tsx
));
      document.documentElement.style.setProperty('--coffee-story-y', `${(pageProgress - 0.18) * -44}px`);
      document.documentElement.style.setProperty('--coffee-story-scale', (1.02 + pageProgress * 0.08).toFixed(3));
      document.documentElement.style.setProperty('--coffee-cinema-scale', (1.04 + pageProgress * 0.045).toFixed(3));
      frame = 0;
    };

    const handleScroll = () => {
      if (frame) return;
      frame = window.requestAnimationFrame(updateCamera);
    };

    updateCamera();
    window.addEventListener('scroll', handleScroll, { passive: true });

    return () => {
      document.documentElement.classList.remove('luxury-home-page');
      document.body.classList.remove('luxury-home-page');
      document.documentElement.style.removeProperty('--coffee-hero-y');
      document.documentElement.style.removeProperty('--coffee-hero-scale');
      document.documentElement.style.removeProperty('--coffee-copy-y');
      document.documentElement.style.removeProperty('--coffee-copy-scale');
      document.documentElement.style.removeProperty('--coffee-story-y');
      document.documentElement.style.removeProperty('--coffee-story-scale');
      document.documentElement.style.removeProperty('--coffee-cinema-scale');
      window.removeEventListener('scroll', handleScroll);
      animatedItems.forEach((item) => observer.unobserve(item));
      if (frame) window.cancelAnimationFrame(frame);
    };
  }, []);

  useEffect(() => {
    const timer = window.setInterval(() => {
      setFeatureIndex((current) => (current + 1) % featureSlides.length);
    }, 3200);

    return () => window.clearInterval(timer);
  }, []);

  const scrollTo = (id: string) => {
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  const featureSlots = [-1, 0, 1].map((offset) => {
    const index = (featureIndex + offset + featureSlides.length) % featureSlides.length;
    return {
      ...featureSlides[index],
      slot: offset === 0 ? 'center' : offset < 0 ? 'left' : 'right'
    };
  });

  return (
    <main className="coffee-home">
      <header className={`coffee-nav${navScrolled ? ' coffee-nav--scrolled' : ''}${navHidden ? ' coffee-nav--hidden' : ''}`} aria-label="Điều hướng chính">
        <div className="coffee-nav__inner">

```
