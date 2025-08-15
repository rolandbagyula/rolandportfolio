#!/usr/bin/env node
/**
 * Build script for Roland's Portfolio
 * Combines Python backend with Node.js frontend optimization
 */

const fs = require('fs');
const path = require('path');

console.log('🚀 Building Roland Portfolio...');

// Build configuration
const config = {
    srcDir: '.',
    distDir: './dist',
    files: {
        html: ['index.html', 'blog.html', 'react-hooks-tutorial.html'],
        css: ['styles.css'],
        js: ['script.js'],
        python: ['flask_test.py', 'portfolio_tools.py', 'simple_demo.py']
    }
};

// Create dist directory if it doesn't exist
if (!fs.existsSync(config.distDir)) {
    fs.mkdirSync(config.distDir);
    console.log('📁 Created dist directory');
}

// Copy HTML files
config.files.html.forEach(file => {
    if (fs.existsSync(file)) {
        const content = fs.readFileSync(file, 'utf8');
        // Simple optimization: remove extra whitespace
        const optimized = content.replace(/\s+/g, ' ').trim();
        fs.writeFileSync(path.join(config.distDir, file), optimized);
        console.log(`✅ Optimized ${file}`);
    }
});

// Copy and optimize CSS
config.files.css.forEach(file => {
    if (fs.existsSync(file)) {
        const content = fs.readFileSync(file, 'utf8');
        // Simple CSS optimization: remove comments and extra spaces
        const optimized = content
            .replace(/\/\*[\s\S]*?\*\//g, '')
            .replace(/\s+/g, ' ')
            .trim();
        fs.writeFileSync(path.join(config.distDir, file), optimized);
        console.log(`✅ Optimized ${file}`);
    }
});

// Copy JavaScript files
config.files.js.forEach(file => {
    if (fs.existsSync(file)) {
        fs.copyFileSync(file, path.join(config.distDir, file));
        console.log(`✅ Copied ${file}`);
    }
});

// Copy Python files (for backend)
config.files.python.forEach(file => {
    if (fs.existsSync(file)) {
        fs.copyFileSync(file, path.join(config.distDir, file));
        console.log(`✅ Copied ${file}`);
    }
});

// Copy images
if (fs.existsSync('főkép.jpg')) {
    fs.copyFileSync('főkép.jpg', path.join(config.distDir, 'főkép.jpg'));
    console.log('✅ Copied főkép.jpg');
}

if (fs.existsSync('headerikon.jpg')) {
    fs.copyFileSync('headerikon.jpg', path.join(config.distDir, 'headerikon.jpg'));
    console.log('✅ Copied headerikon.jpg');
}

console.log('🎉 Build complete!');
console.log(`📦 Files built to: ${config.distDir}`);
console.log('💡 Next steps:');
console.log('   - Run Python backend: python flask_test.py');
console.log('   - Serve static files: python -m http.server 8000');
console.log('   - Deploy to production');
