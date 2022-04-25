import MainPageApp from './MainPageApp.svelte';
import { defaults } from './defaults.js';

let params = new URLSearchParams(window.location.search);
for (let i of Object.keys(defaults)) {
    if (!params.has(i)) { 
        params.append(i, params.get(i));
    } 
}

let child = document.createElement('style');
child.innerHTML = `body { 
    background-color: ${params.get('background')};
}`;
document.body.appendChild(child);

const app = new MainPageApp({
    target: document.body,
    props: {
        'params': params
    }
});

export default app;