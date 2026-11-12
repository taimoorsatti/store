import express, { Request, Response } from 'express';
import path from 'path';
import fs from 'fs';
import { Liquid } from 'liquidjs';

const app = express();
const PORT = process.env.PORT ? parseInt(process.env.PORT, 10) : 3000;

// Body parsing
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static assets directly from /assets and /public
app.use('/assets', express.static(path.join(process.cwd(), 'assets')));
app.use('/public', express.static(path.join(process.cwd(), 'public')));

// Serve the downloadable Shopify Theme ZIP files
const serveZip = (filename: string) => (_req: Request, res: Response) => {
  const zipPath = path.join(process.cwd(), filename);
  if (fs.existsSync(zipPath)) {
    res.setHeader('Content-Disposition', `attachment; filename="${filename}"`);
    res.setHeader('Content-Type', 'application/zip');
    res.sendFile(zipPath);
  } else {
    res.status(404).send('Theme ZIP not found. Please run packager.');
  }
};

app.get('/FABFaddons-Premium-Shopify-Theme.zip', serveZip('FABFaddons-Premium-Shopify-Theme.zip'));
app.get('/FABFaddons-Shopify-Theme.zip', serveZip('FABFaddons-Shopify-Theme.zip'));

// Load Locales
const enLocale = JSON.parse(fs.readFileSync(path.join(process.cwd(), 'locales', 'en.default.json'), 'utf8'));
const arLocale = JSON.parse(fs.readFileSync(path.join(process.cwd(), 'locales', 'ar.json'), 'utf8'));

// Load Settings
let settingsData: Record<string, any> = {};
try {
  const rawSettings = fs.readFileSync(path.join(process.cwd(), 'config', 'settings_data.json'), 'utf8');
  const parsed = JSON.parse(rawSettings);
  settingsData = parsed.current || {};
} catch {
  settingsData = {
    color_primary: '#351C27',
    color_background: '#F7F3ED',
    color_accent: '#C5A477',
    color_secondary_bg: '#E9DFD5',
    color_text_primary: '#29231F',
    color_text_muted: '#766B64',
    cart_drawer_enabled: true,
    free_shipping_threshold: 250,
    currency_code: 'AED'
  };
}

// 6 Curated Launch Products for FABFaddons
export interface Product {
  id: number;
  title: string;
  title_ar: string;
  handle: string;
  type: string;
  vendor: string;
  price: number;
  compare_at_price: number;
  available: boolean;
  sales_rank: number;
  created_at: string;
  url: string;
  featured_media: { src: string };
  media: Array<{ src: string }>;
  description: string;
  description_ar: string;
  selected_or_first_available_variant: { id: number; title: string; price: number; compare_at_price: number; available: boolean };
  variants: Array<{ id: number; title: string; price: number; compare_at_price: number; available: boolean }>;
}

const PRODUCTS: Product[] = [
  {
    id: 1,
    title: 'Sonic Facial Sculpting & Deep Cleansing Device',
    title_ar: 'جهاز تنظيف ونحت الوجه الصوتي المتطور',
    handle: 'sonic-cleansing-device',
    type: 'Facial Devices',
    vendor: 'FABFaddons Dubai',
    price: 34900,
    compare_at_price: 49900,
    available: true,
    sales_rank: 1,
    created_at: '2026-01-15T00:00:00Z',
    url: '/products/sonic-cleansing-device',
    featured_media: { src: '/assets/product-sonic-cleansing-device.jpg' },
    media: [
      { src: '/assets/product-sonic-cleansing-device.jpg' },
      { src: '/assets/hero-luxury-beauty-ritual.jpg' }
    ],
    description: 'Transform your daily skincare ritual with medical-grade ultra-sonic vibrations designed to decongest pores, enhance lymphatic drainage, and sculpt facial contours with precision.',
    description_ar: 'ارتقي بروتينك اليومي مع تقنية الاهتزازات الصوتية الطبية لتنقية المسام بعمق، تحفيز التصريف اللمفاوي، ونحت ملامح الوجه بجاذبية استثنائية.',
    selected_or_first_available_variant: { id: 101, title: 'Pearl Rose Gold', price: 34900, compare_at_price: 49900, available: true },
    variants: [
      { id: 101, title: 'Pearl Rose Gold', price: 34900, compare_at_price: 49900, available: true },
      { id: 102, title: 'Obsidian Noir', price: 34900, compare_at_price: 49900, available: true },
      { id: 103, title: 'Champagne Gold', price: 34900, compare_at_price: 49900, available: true }
    ]
  },
  {
    id: 2,
    title: 'Rose Quartz Facial Sculpting Roller & Gua Sha Set',
    title_ar: 'مجموعة رولر وغوا شا من الكوارتز الوردي الطبيعي',
    handle: 'rose-quartz-sculpting-set',
    type: 'Sculpting & Gua Sha',
    vendor: 'FABFaddons Dubai',
    price: 17900,
    compare_at_price: 24900,
    available: true,
    sales_rank: 2,
    created_at: '2026-02-01T00:00:00Z',
    url: '/products/rose-quartz-sculpting-set',
    featured_media: { src: '/assets/product-rose-quartz-sculpting-set.jpg' },
    media: [
      { src: '/assets/product-rose-quartz-sculpting-set.jpg' },
      { src: '/assets/hero-luxury-beauty-ritual.jpg' }
    ],
    description: 'Carved from 100% natural certified Brazilian rose quartz. Calms inflamed skin, releases facial tension, and accelerates cellular serum absorption.',
    description_ar: 'منحوتة يدوياً من حجر الكوارتز الوردي البرازيلي الطبيعي 100%. تهدئ البشرة، تزيل انتفاخ الصباح، وتزيد من فعالية امتصاص السيروم.',
    selected_or_first_available_variant: { id: 201, title: 'Brazilian Rose Quartz', price: 17900, compare_at_price: 24900, available: true },
    variants: [
      { id: 201, title: 'Brazilian Rose Quartz', price: 17900, compare_at_price: 24900, available: true },
      { id: 202, title: 'Imperial Jade Green', price: 17900, compare_at_price: 24900, available: true }
    ]
  },
  {
    id: 3,
    title: 'Multi-Wave 7-Color LED Light Therapy Face Mask',
    title_ar: 'قناع العلاج بالضوء LED سباعي الأطياف لتجديد البشرة',
    handle: 'led-light-therapy-mask',
    type: 'LED Light Therapy',
    vendor: 'FABFaddons Dubai',
    price: 58900,
    compare_at_price: 79900,
    available: true,
    sales_rank: 3,
    created_at: '2026-02-10T00:00:00Z',
    url: '/products/led-light-therapy-mask',
    featured_media: { src: '/assets/product-led-light-therapy-mask.jpg' },
    media: [
      { src: '/assets/product-led-light-therapy-mask.jpg' },
      { src: '/assets/campaign-editorial-banner.jpg' }
    ],
    description: 'Clinical grade phototherapy mask featuring Red, Blue, Near-Infrared and Amber LED spectrums to trigger collagen synthesis and eradicate impurities.',
    description_ar: 'قناع الفوتوثيرابي المعتمد سريرياً بـ 7 أطياف ضوئية لتحفيز إنتاج الكولاجين، تفتيح التصبغات، وعلاج حب الشباب من أول جلسة.',
    selected_or_first_available_variant: { id: 301, title: 'Pearl White & Gold Trim', price: 58900, compare_at_price: 79900, available: true },
    variants: [
      { id: 301, title: 'Pearl White & Gold Trim', price: 58900, compare_at_price: 79900, available: true },
      { id: 302, title: 'Velvet Burgundy Edition', price: 58900, compare_at_price: 79900, available: true }
    ]
  },
  {
    id: 4,
    title: 'Multi-Styler Thermal Ceramic Airwrap & Volumizer',
    title_ar: 'مصفف ومجفف الشعر الحراري متعدد الرؤوس بالسيراميك',
    handle: 'ceramic-airwrap-styler',
    type: 'Hair Styling',
    vendor: 'FABFaddons Dubai',
    price: 42900,
    compare_at_price: 59900,
    available: true,
    sales_rank: 4,
    created_at: '2026-03-01T00:00:00Z',
    url: '/products/ceramic-airwrap-styler',
    featured_media: { src: '/assets/product-ceramic-airwrap-styler.jpg' },
    media: [
      { src: '/assets/product-ceramic-airwrap-styler.jpg' },
      { src: '/assets/hero-luxury-beauty-ritual.jpg' }
    ],
    description: 'Aerodynamic airflow styling without extreme heat damage. Includes 5 interchangeable luxury barrels for salon curls, silky blowouts, and smoothing.',
    description_ar: 'تصفيف هوائي ديناميكي بدون تلف حراري مفرط. يشمل 5 رؤوس فاخرة قابلة للتبديل للتجعيد والتنعيم وتجفيف الصالونات الاحترافي.',
    selected_or_first_available_variant: { id: 401, title: 'Champagne Gold & Rose', price: 42900, compare_at_price: 59900, available: true },
    variants: [
      { id: 401, title: 'Champagne Gold & Rose', price: 42900, compare_at_price: 59900, available: true },
      { id: 402, title: 'Burgundy Luxe', price: 42900, compare_at_price: 59900, available: true }
    ]
  },
  {
    id: 5,
    title: 'Multi-Peptide Cellular Repair Elixir Serum',
    title_ar: 'سيروم الببتيدات المتعددة للترميم الخلوي والنضارة',
    handle: 'peptide-elixir-serum',
    type: 'Botanical Skincare',
    vendor: 'FABFaddons Dubai',
    price: 21900,
    compare_at_price: 29900,
    available: true,
    sales_rank: 5,
    created_at: '2026-03-15T00:00:00Z',
    url: '/products/peptide-elixir-serum',
    featured_media: { src: '/assets/product-peptide-elixir-serum.jpg' },
    media: [
      { src: '/assets/product-peptide-elixir-serum.jpg' },
      { src: '/assets/campaign-editorial-banner.jpg' }
    ],
    description: 'Ultra-concentrated botanical peptides, hyaluronic acid spheres, and 24K gold flakes suspended in a silky elixir to restore youthful elasticity and luminous hydration.',
    description_ar: 'مزيج فائق التركيز من ببتيدات الترميم النباتية، حمض الهيالورونيك، ورقائق الذهب عيار 24 لمرونة ونضارة حريرية تدوم طوال اليوم.',
    selected_or_first_available_variant: { id: 501, title: '30ml Luxury Dropper', price: 21900, compare_at_price: 29900, available: true },
    variants: [
      { id: 501, title: '30ml Luxury Dropper', price: 21900, compare_at_price: 29900, available: true },
      { id: 502, title: '50ml Grand Edition', price: 31900, compare_at_price: 39900, available: true }
    ]
  },
  {
    id: 6,
    title: 'Rotating 360° Luxury Acrylic Cosmetics Organizer',
    title_ar: 'منظم مستحضرات التجميل الدوار 360° الفاخر من الأكريليك',
    handle: 'luxury-cosmetics-organizer',
    type: 'Vanity & Storage',
    vendor: 'FABFaddons Dubai',
    price: 15900,
    compare_at_price: 22900,
    available: true,
    sales_rank: 6,
    created_at: '2026-04-01T00:00:00Z',
    url: '/products/luxury-cosmetics-organizer',
    featured_media: { src: '/assets/product-luxury-cosmetics-organizer.jpg' },
    media: [
      { src: '/assets/product-luxury-cosmetics-organizer.jpg' },
      { src: '/assets/hero-luxury-beauty-ritual.jpg' }
    ],
    description: 'Architectural diamond-cut acrylic vanity tower with 360-degree silent rotation. Holds up to 60 cosmetic bottles, brushes, and palettes in immaculate luxury order.',
    description_ar: 'برج تسريحة هندسي مصنوع من الأكريليك النقي المقاوم للخدش مع دوران صامت 360 درجة. يتسع لأكثر من 60 منتج تجميل وفرشاة بأناقة.',
    selected_or_first_available_variant: { id: 601, title: 'Diamond Crystal Clear', price: 15900, compare_at_price: 22900, available: true },
    variants: [
      { id: 601, title: 'Diamond Crystal Clear', price: 15900, compare_at_price: 22900, available: true },
      { id: 602, title: 'Smoked Amber Gold', price: 15900, compare_at_price: 22900, available: true }
    ]
  }
];

// In-Memory Cart for preview & live testing
interface CartItem {
  id: number;
  product_id: number;
  variant_id: number;
  title: string;
  price: number;
  quantity: number;
  image?: string;
  final_line_price: number;
  product: any;
  variant: any;
  url: string;
}

let cartState = {
  item_count: 0,
  total_price: 0,
  items: [] as CartItem[]
};

function recalculateCart() {
  cartState.item_count = cartState.items.reduce((sum, item) => sum + item.quantity, 0);
  cartState.total_price = cartState.items.reduce((sum, item) => sum + item.final_line_price, 0);
}

// LiquidJS Engine Setup
const engine = new Liquid({
  root: [process.cwd(), path.join(process.cwd(), 'layout'), path.join(process.cwd(), 'templates'), path.join(process.cwd(), 'sections'), path.join(process.cwd(), 'snippets')],
  extname: '.liquid',
  dynamicPartials: true
});

function sanitizeShopify(str: string): string {
  return str
    .replace(/{%\s*schema\s*%}[\s\S]*?{%\s*endschema\s*%}/g, '')
    .replace(/{%\s*form\s+['"]?([a-zA-Z0-9_-]+)['"]?[^%]*%}/g, '<form method="post" action="/cart/add" class="shopify-form-$1">')
    .replace(/{%\s*endform\s*%}/g, '</form>');
}

engine.registerTag('schema', {
  parse: function(_tagToken: any, remainTokens: any) {
    while (remainTokens.length) {
      if (remainTokens.shift().name === 'endschema') break;
    }
  },
  render: function() { return ''; }
});

engine.registerTag('section', {
  parse: function(token: any) {
    this.sectionName = token.args.replace(/['"]/g, '').trim();
  },
  render: async function(scope: any) {
    const filePath = path.join(process.cwd(), 'sections', `${this.sectionName}.liquid`);
    if (!fs.existsSync(filePath)) return `<!-- section ${this.sectionName} not found -->`;
    const content = sanitizeShopify(fs.readFileSync(filePath, 'utf8'));
    return engine.parseAndRender(content, scope.getAll());
  }
});

// Translation lookup
function getTranslation(dict: any, key: string): string {
  const parts = key.split('.');
  let cur = dict;
  for (const p of parts) {
    if (!cur || typeof cur !== 'object') return key;
    cur = cur[p];
  }
  return typeof cur === 'string' ? cur : key;
}

// Filters
engine.registerFilter('asset_url', (v: any) => `/assets/${v}`);
engine.registerFilter('stylesheet_tag', (v: any) => `<link rel="stylesheet" href="${v}">`);
engine.registerFilter('script_tag', (v: any) => `<script src="${v}"></script>`);
engine.registerFilter('image_url', (v: any, _opts: any) => {
  if (typeof v === 'string') return v.startsWith('/') ? v : `/assets/${v}`;
  return v?.src || '/assets/hero-luxury-beauty-ritual.jpg';
});
engine.registerFilter('image_tag', (url: any, attrs: any) => `<img src="${url}" ${attrs ? 'class="' + attrs + '"' : ''} />`);
engine.registerFilter('money', (v: any) => {
  const num = typeof v === 'number' ? (v > 1000 ? Math.round(v / 100) : v) : v;
  return `AED ${num}`;
});
engine.registerFilter('payment_button', () => `<button type="submit" class="btn-primary" style="width:100%; margin-top: 0.5rem; background: var(--color-accent); color: var(--color-primary);">Buy It Now · Express Checkout</button>`);
engine.registerFilter('handle', (v: any) => String(v).toLowerCase().replace(/[^a-z0-9]+/g, '-'));
engine.registerFilter('t', function(this: any, key: string, opts?: Record<string, any>) {
  const isAr = this.context.get(['request', 'locale', 'iso_code']) === 'ar';
  let str = getTranslation(isAr ? arLocale : enLocale, key);
  if (opts && typeof str === 'string') {
    for (const [k, val] of Object.entries(opts)) {
      str = str.replace(new RegExp(`{{\\s*${k}\\s*}}`, 'g'), String(val));
    }
  }
  return str;
});

// Helper to render Shopify OS 2.0 JSON templates
async function renderJsonTemplate(templateName: string, context: Record<string, any>): Promise<string> {
  const jsonPath = path.join(process.cwd(), 'templates', `${templateName}.json`);
  if (!fs.existsSync(jsonPath)) {
    return `<div class="container" style="padding: 4rem 0;"><h2>Template ${templateName} not found</h2></div>`;
  }

  const json = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
  let html = '';

  for (const sectionId of json.order || []) {
    const sectionConfig = json.sections[sectionId];
    if (!sectionConfig) continue;
    const secFile = path.join(process.cwd(), 'sections', `${sectionConfig.type}.liquid`);
    if (fs.existsSync(secFile)) {
      const secContent = sanitizeShopify(fs.readFileSync(secFile, 'utf8'));
      const secScope = {
        ...context,
        section: {
          id: sectionId,
          settings: sectionConfig.settings || {},
          blocks: sectionConfig.blocks || {}
        }
      };
      html += await engine.parseAndRender(secContent, secScope);
    }
  }

  return html;
}

// Master layout renderer
async function renderTheme(req: Request, res: Response, contentHtml: string, pageTitle: string, templateName = 'index', extraContext: Record<string, any> = {}) {
  const locale = (req.query.locale as string) || (req.headers['accept-language']?.includes('ar') ? 'ar' : 'en');
  const isAr = locale === 'ar';

  const downloadNotice = `
    <div style="background: linear-gradient(90deg, #351C27 0%, #201117 100%); color: #F7F3ED; padding: 0.6rem 1.25rem; border-bottom: 1px solid rgba(197, 164, 119, 0.4); font-size: 0.78rem; text-align: center; display: flex; align-items: center; justify-content: center; gap: 1rem; flex-wrap: wrap; z-index: 9999; position: relative;">
      <span>💎 <strong>FABFaddons</strong> Premium Shopify Online Store 2.0 Theme · Dubai UAE Edition</span>
      <a href="/FABFaddons-Premium-Shopify-Theme.zip" download="FABFaddons-Premium-Shopify-Theme.zip" class="btn-accent" style="padding: 0.4rem 1rem; font-size: 11px; border-radius: 3px; text-decoration: none; display: inline-flex; align-items: center; gap: 0.4rem; color: #351C27; background: #C5A477; font-weight: 700;">
        <svg width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
        Download Theme ZIP (FABFaddons-Premium-Shopify-Theme.zip)
      </a>
      <span style="opacity: 0.75; font-size: 0.72rem;">Shopify Admin &rarr; Online Store &rarr; Themes &rarr; Upload ZIP</span>
    </div>
  `;

  const layoutContext = {
    request: {
      locale: { iso_code: isAr ? 'ar' : 'en' },
      origin: `${req.protocol}://${req.get('host')}`
    },
    page_title: `${pageTitle} — FABFaddons | Luxury Beauty & Cosmetics UAE`,
    page_description: 'Modern luxury beauty, skincare and cosmetics dropshipping storefront for the UAE market. Beauty. Confidence. You.',
    canonical_url: `${req.protocol}://${req.get('host')}${req.path}`,
    routes: {
      root_url: `/?locale=${locale}`,
      all_products_collection_url: `/collections/all?locale=${locale}`,
      search_url: `/search?locale=${locale}`,
      cart_url: `/cart?locale=${locale}`,
      cart_add_url: '/cart/add.js',
      cart_change_url: '/cart/change.js',
      cart_update_url: '/cart/update.js',
      predictive_search_url: '/search/suggest.js'
    },
    shop: {
      name: 'FABFaddons'
    },
    cart: cartState,
    settings: settingsData,
    collections: {
      all: {
        title: isAr ? 'جميع مستحضرات التجميل' : 'All Beauty Essentials',
        products: PRODUCTS
      }
    },
    all_products: PRODUCTS.reduce((acc, p) => ({ ...acc, [p.handle]: p }), {}),
    content_for_header: '<!-- Shopify Theme Header -->',
    content_for_layout: contentHtml,
    template: { name: templateName },
    ...extraContext
  };

  const layoutContent = fs.readFileSync(path.join(process.cwd(), 'layout', 'theme.liquid'), 'utf8');
  let fullHtml = await engine.parseAndRender(layoutContent, layoutContext);

  // Inject luxury download banner right after <body>
  fullHtml = fullHtml.replace('<body', downloadNotice + '<body');

  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.send(fullHtml);
}

// -------------------------------------------------------------------------
// ADVANCED COLLECTION FILTERING & SORTING ARCHITECTURE
// -------------------------------------------------------------------------

function buildCollectionData(req: Request) {
  const query = req.query as Record<string, string>;
  const locale = (query.locale as string) || 'en';
  const isAr = locale === 'ar';
  const sortBy = query.sort_by || 'manual';

  // Active filter params
  const availabilityFilter = query['filter.v.availability']; // '1' or '0'
  const typeFilter = query['filter.p.product_type']; // category string
  const vendorFilter = query['filter.p.vendor']; // vendor string
  const priceMin = query['filter.v.price.gte'] ? parseFloat(query['filter.v.price.gte']) : null;
  const priceMax = query['filter.v.price.lte'] ? parseFloat(query['filter.v.price.lte']) : null;

  // 1. Filter products
  let filtered = [...PRODUCTS];

  if (availabilityFilter !== undefined) {
    const isAvail = availabilityFilter === '1';
    filtered = filtered.filter(p => p.available === isAvail);
  }

  if (typeFilter) {
    const target = typeFilter.toLowerCase();
    filtered = filtered.filter(p => p.type.toLowerCase() === target);
  }

  if (vendorFilter) {
    const target = vendorFilter.toLowerCase();
    filtered = filtered.filter(p => p.vendor.toLowerCase() === target);
  }

  if (priceMin !== null) {
    filtered = filtered.filter(p => (p.price / 100) >= priceMin);
  }

  if (priceMax !== null) {
    filtered = filtered.filter(p => (p.price / 100) <= priceMax);
  }

  // 2. Sort products
  switch (sortBy) {
    case 'price-ascending':
      filtered.sort((a, b) => a.price - b.price);
      break;
    case 'price-descending':
      filtered.sort((a, b) => b.price - a.price);
      break;
    case 'title-ascending':
      filtered.sort((a, b) => a.title.localeCompare(b.title));
      break;
    case 'title-descending':
      filtered.sort((a, b) => b.title.localeCompare(a.title));
      break;
    case 'best-selling':
      filtered.sort((a, b) => a.sales_rank - b.sales_rank);
      break;
    case 'created-descending':
      filtered.sort((a, b) => b.id - a.id);
      break;
    case 'created-ascending':
      filtered.sort((a, b) => a.id - b.id);
      break;
    case 'manual':
    default:
      // Keep default curated order
      break;
  }

  // Helper to build filter query string
  function getUrlWithParam(param: string, value: string | null) {
    const q = { ...query };
    if (value === null) {
      delete q[param];
    } else {
      q[param] = value;
    }
    const searchParams = new URLSearchParams(q);
    return `/collections/all?${searchParams.toString()}`;
  }

  // 3. Build native collection.filters structure
  const types = Array.from(new Set(PRODUCTS.map(p => p.type)));
  const typeValues = types.map(t => {
    const isActive = typeFilter?.toLowerCase() === t.toLowerCase();
    const count = PRODUCTS.filter(p => p.type.toLowerCase() === t.toLowerCase()).length;
    return {
      label: t,
      value: t,
      count,
      active: isActive,
      param_name: 'filter.p.product_type',
      url_to_add: getUrlWithParam('filter.p.product_type', t),
      url_to_remove: getUrlWithParam('filter.p.product_type', null)
    };
  });

  const availabilityValues = [
    {
      label: isAr ? 'متوفر حالياً' : 'In stock',
      value: '1',
      count: PRODUCTS.filter(p => p.available).length,
      active: availabilityFilter === '1',
      param_name: 'filter.v.availability',
      url_to_add: getUrlWithParam('filter.v.availability', '1'),
      url_to_remove: getUrlWithParam('filter.v.availability', null)
    },
    {
      label: isAr ? 'غير متوفر' : 'Out of stock',
      value: '0',
      count: PRODUCTS.filter(p => !p.available).length,
      active: availabilityFilter === '0',
      param_name: 'filter.v.availability',
      url_to_add: getUrlWithParam('filter.v.availability', '0'),
      url_to_remove: getUrlWithParam('filter.v.availability', null)
    }
  ];

  const filters = [
    {
      label: isAr ? 'التوفر' : 'Availability',
      type: 'list',
      param_name: 'filter.v.availability',
      active_values: availabilityValues.filter(v => v.active),
      values: availabilityValues
    },
    {
      label: isAr ? 'نطاق السعر (درهم)' : 'Price Range (AED)',
      type: 'price_range',
      param_name: 'filter.v.price',
      range_max: 799,
      min_value: {
        param_name: 'filter.v.price.gte',
        value: priceMin
      },
      max_value: {
        param_name: 'filter.v.price.lte',
        value: priceMax
      },
      url_to_remove: (() => {
        const q = { ...query };
        delete q['filter.v.price.gte'];
        delete q['filter.v.price.lte'];
        return `/collections/all?${new URLSearchParams(q).toString()}`;
      })()
    },
    {
      label: isAr ? 'نوع المنتج' : 'Category',
      type: 'list',
      param_name: 'filter.p.product_type',
      active_values: typeValues.filter(v => v.active),
      values: typeValues
    }
  ];

  // Sort Options
  const sortOptions = [
    { value: 'manual', name: isAr ? 'المقترحات المميزة' : 'Featured' },
    { value: 'best-selling', name: isAr ? 'الأكثر مبيعاً' : 'Best Selling' },
    { value: 'title-ascending', name: isAr ? 'أبجدياً، أ–ي' : 'Alphabetically, A–Z' },
    { value: 'title-descending', name: isAr ? 'أبجدياً، ي–أ' : 'Alphabetically, Z–A' },
    { value: 'price-ascending', name: isAr ? 'السعر، من الأقل للأعلى' : 'Price, Low to High' },
    { value: 'price-descending', name: isAr ? 'السعر، من الأعلى للأقل' : 'Price, High to Low' },
    { value: 'created-descending', name: isAr ? 'الأحدث أولاً' : 'Date, New to Old' },
    { value: 'created-ascending', name: isAr ? 'الأقدم أولاً' : 'Date, Old to New' }
  ];

  return {
    title: isAr ? 'جميع مستحضرات التجميل' : 'The Launch Collection',
    description: isAr ? 'ستة منتجات تجميلية استثنائية صُممت بأعلى معايير الرفاهية العصرية في الإمارات.' : 'Discover our complete curation of medical-grade skincare devices, botanical elixirs, and luxury vanity essentials.',
    url: '/collections/all',
    products: filtered,
    products_count: filtered.length,
    filters,
    sort_options: sortOptions,
    sort_by: sortBy,
    default_sort_by: 'manual'
  };
}

// -------------------------------------------------------------------------
// ROUTES
// -------------------------------------------------------------------------

// Homepage
app.get('/', async (req: Request, res: Response) => {
  try {
    const locale = (req.query.locale as string) || 'en';
    const bodyHtml = await renderJsonTemplate('index', {
      collections: {
        all: { products: PRODUCTS }
      },
      request: { locale: { iso_code: locale } }
    });
    await renderTheme(req, res, bodyHtml, 'Beauty. Confidence. You.', 'index');
  } catch (err: any) {
    console.error('Render error:', err);
    res.status(500).send(`Theme render error: ${err.message}`);
  }
});

// Collection Page with full Native Filtering & Sorting
app.get('/collections/:handle', async (req: Request, res: Response) => {
  try {
    const locale = (req.query.locale as string) || 'en';
    const collectionData = buildCollectionData(req);

    const bodyHtml = await renderJsonTemplate('collection', {
      collection: collectionData,
      request: { locale: { iso_code: locale } }
    });
    await renderTheme(req, res, bodyHtml, collectionData.title, 'collection', { collection: collectionData });
  } catch (err: any) {
    console.error('Collection error:', err);
    res.status(500).send(`Collection error: ${err.message}`);
  }
});

// Product Details Page
app.get('/products/:handle', async (req: Request, res: Response) => {
  try {
    const { handle } = req.params;
    const locale = (req.query.locale as string) || 'en';
    const product = PRODUCTS.find(p => p.handle === handle) || PRODUCTS[0];
    const relatedProducts = PRODUCTS.filter(p => p.id !== product.id).slice(0, 3);

    const bodyHtml = await renderJsonTemplate('product', {
      product,
      recommendations: { products: relatedProducts },
      collections: { all: { products: relatedProducts } },
      request: { locale: { iso_code: locale } }
    });
    await renderTheme(req, res, bodyHtml, product.title, 'product', { product });
  } catch (err: any) {
    res.status(500).send(`Product error: ${err.message}`);
  }
});

// Cart Page
app.get('/cart', async (req: Request, res: Response) => {
  try {
    const locale = (req.query.locale as string) || 'en';
    const bodyHtml = await renderJsonTemplate('cart', {
      cart: cartState,
      request: { locale: { iso_code: locale } }
    });
    await renderTheme(req, res, 'Shopping Bag', 'cart');
  } catch (err: any) {
    res.status(500).send(`Cart error: ${err.message}`);
  }
});

// Search Page
app.get('/search', async (req: Request, res: Response) => {
  try {
    const q = ((req.query.q as string) || '').toLowerCase();
    const locale = (req.query.locale as string) || 'en';
    const results = q ? PRODUCTS.filter(p => p.title.toLowerCase().includes(q) || p.description.toLowerCase().includes(q) || p.type.toLowerCase().includes(q)) : PRODUCTS;
    const bodyHtml = await renderJsonTemplate('search', {
      search: {
        terms: q,
        performed: true,
        results,
        results_count: results.length
      },
      request: { locale: { iso_code: locale } }
    });
    await renderTheme(req, res, `Search: ${q || 'All'}`, 'search');
  } catch (err: any) {
    res.status(500).send(`Search error: ${err.message}`);
  }
});

// Content Pages (about, contact, faq, policies)
app.get('/pages/:handle', async (req: Request, res: Response) => {
  try {
    const { handle } = req.params;
    const locale = (req.query.locale as string) || 'en';
    let templateName = 'page';
    if (['about', 'contact', 'faq', 'policy'].includes(handle)) {
      templateName = `page.${handle}`;
    }

    const titles: Record<string, string> = {
      about: 'About FABFaddons Dubai',
      contact: 'Client Concierge & Inquiries',
      faq: 'Frequently Asked Questions',
      'shipping-policy': 'UAE Express Delivery & Shipping Policy',
      'returns-policy': 'Returns & Exchange Policy',
      'privacy-policy': 'Privacy Policy',
      terms: 'Terms of Service'
    };

    const bodyHtml = await renderJsonTemplate(templateName, {
      page: {
        title: titles[handle] || handle.replace(/-/g, ' ').toUpperCase(),
        content: '<p>FABFaddons is committed to curating the finest international luxury beauty innovations for modern women in the UAE. For immediate concierge assistance, reach us at concierge@fabfaddons.ae.</p>'
      },
      request: { locale: { iso_code: locale } }
    });
    await renderTheme(req, res, titles[handle] || 'Store Policy', 'page');
  } catch (err: any) {
    res.status(500).send(`Page error: ${err.message}`);
  }
});

// -------------------------------------------------------------------------
// SHOPIFY AJAX CART API ENDPOINTS
// -------------------------------------------------------------------------

app.get('/cart.js', (_req: Request, res: Response) => {
  res.json(cartState);
});

app.post('/cart/add.js', (req: Request, res: Response) => {
  const variantId = parseInt(req.body.id, 10);
  const qty = parseInt(req.body.quantity, 10) || 1;

  let foundProduct: any = null;
  let foundVariant: any = null;

  for (const p of PRODUCTS) {
    const v = p.variants.find(item => item.id === variantId);
    if (v) {
      foundProduct = p;
      foundVariant = v;
      break;
    }
  }

  if (!foundProduct) {
    foundProduct = PRODUCTS[0];
    foundVariant = foundProduct.variants[0];
  }

  const existing = cartState.items.find(item => item.variant_id === foundVariant.id);
  if (existing) {
    existing.quantity += qty;
    existing.final_line_price = existing.quantity * existing.price;
  } else {
    cartState.items.push({
      id: Date.now(),
      product_id: foundProduct.id,
      variant_id: foundVariant.id,
      title: `${foundProduct.title} - ${foundVariant.title}`,
      price: foundVariant.price,
      quantity: qty,
      image: foundProduct.featured_media.src,
      final_line_price: foundVariant.price * qty,
      product: foundProduct,
      variant: foundVariant,
      url: foundProduct.url
    });
  }

  recalculateCart();
  res.json(cartState);
});

app.post('/cart/change.js', (req: Request, res: Response) => {
  const line = parseInt(req.body.line, 10);
  const qty = parseInt(req.body.quantity, 10);
  const variantId = parseInt(req.body.id, 10);

  if (!isNaN(line) && line >= 1 && line <= cartState.items.length) {
    if (qty <= 0) {
      cartState.items.splice(line - 1, 1);
    } else {
      cartState.items[line - 1].quantity = qty;
      cartState.items[line - 1].final_line_price = qty * cartState.items[line - 1].price;
    }
  } else if (!isNaN(variantId)) {
    const itemIndex = cartState.items.findIndex(i => i.variant_id === variantId);
    if (itemIndex > -1) {
      if (qty <= 0) {
        cartState.items.splice(itemIndex, 1);
      } else {
        cartState.items[itemIndex].quantity = qty;
        cartState.items[itemIndex].final_line_price = qty * cartState.items[itemIndex].price;
      }
    }
  }

  recalculateCart();
  res.json(cartState);
});

app.post('/cart/add', (req: Request, res: Response) => {
  const variantId = parseInt(req.body.id, 10);
  const qty = parseInt(req.body.quantity, 10) || 1;

  let foundProduct: any = null;
  let foundVariant: any = null;

  for (const p of PRODUCTS) {
    const v = p.variants.find(item => item.id === variantId);
    if (v) {
      foundProduct = p;
      foundVariant = v;
      break;
    }
  }

  if (!foundProduct) {
    foundProduct = PRODUCTS[0];
    foundVariant = foundProduct.variants[0];
  }

  const existing = cartState.items.find(item => item.variant_id === foundVariant.id);
  if (existing) {
    existing.quantity += qty;
    existing.final_line_price = existing.quantity * existing.price;
  } else {
    cartState.items.push({
      id: Date.now(),
      product_id: foundProduct.id,
      variant_id: foundVariant.id,
      title: `${foundProduct.title} - ${foundVariant.title}`,
      price: foundVariant.price,
      quantity: qty,
      image: foundProduct.featured_media.src,
      final_line_price: foundVariant.price * qty,
      product: foundProduct,
      variant: foundVariant,
      url: foundProduct.url
    });
  }

  recalculateCart();
  res.redirect('/cart');
});

app.post('/cart/clear.js', (_req: Request, res: Response) => {
  cartState.items = [];
  recalculateCart();
  res.json(cartState);
});

// Checkout Mock
app.get('/checkout', (_req: Request, res: Response) => {
  res.send(`
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Shopify Checkout — FABFaddons</title>
        <link rel="stylesheet" href="/assets/theme.css">
        <style>
          body { background: #F7F3ED; display: flex; align-items: center; justify-content: center; min-height: 100vh; padding: 2rem; font-family: 'Plus Jakarta Sans', sans-serif; }
          .checkout-card { background: #FFFFFF; border-radius: 8px; padding: 2.5rem; max-width: 520px; width: 100%; box-shadow: 0 10px 30px rgba(53,28,39,0.08); text-align: center; }
        </style>
      </head>
      <body>
        <div class="checkout-card">
          <div style="font-family: 'Playfair Display', serif; font-size: 1.8rem; font-weight: 700; color: #351C27; margin-bottom: 0.5rem;">FABFaddons</div>
          <div style="font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase; color: #766B64; margin-bottom: 1.5rem;">Native Shopify Checkout</div>
          <div style="background: rgba(197, 164, 119, 0.15); border: 1px solid #C5A477; border-radius: 6px; padding: 1.25rem; margin-bottom: 1.5rem; text-align: left;">
            <div style="font-weight: 700; color: #351C27; font-size: 0.95rem; margin-bottom: 0.5rem;">Ready for Shopify Payments & UAE Gateways</div>
            <p style="font-size: 0.8rem; color: #766B64; line-height: 1.5;">When uploaded to your live Shopify store, this redirects directly to your store's SSL-secured Shopify checkout with Apple Pay, Visa, Mastercard, Tabby, and Cash on Delivery.</p>
          </div>
          <div style="display: flex; gap: 1rem; justify-content: center;">
            <a href="/cart" class="btn-secondary" style="padding: 0.75rem 1.5rem;">Return to Bag</a>
            <a href="/" class="btn-primary" style="padding: 0.75rem 1.5rem;">Continue Shopping</a>
          </div>
        </div>
      </body>
    </html>
  `);
});

// Start Server
app.listen(PORT, '0.0.0.0', () => {
  console.log(`[Shopify OS 2.0 Theme Server] Running on http://0.0.0.0:${PORT}`);
  console.log(`[Shopify OS 2.0 Theme Server] Download Theme ZIP: http://0.0.0.0:${PORT}/FABFaddons-Premium-Shopify-Theme.zip`);
});
