
import { test } from '@playwright/test';
import { expect } from '@playwright/test';

test('ThreeJSModelTest_2026-03-23', async ({ page, context }) => {
  
    // Navigate to URL
    await page.goto('https://threejs.org/examples/', { waitUntil: 'networkidle' });

    // Click element
    await page.click('#container a');

    // Click element
    await page.click('#content div a');

    // Navigate to URL
    await page.goto('https://threejs.org/examples/#webgl_animation_cloth', { waitUntil: 'networkidle' });

    // Click element
    await page.click('div.card > a');

    // Navigate to URL
    await page.goto('https://threejs.org/examples/webgl_animation_keyframes.html', { waitUntil: 'networkidle' });
});