<script>
    import { onMount } from "svelte";


    let sets = fetch('/data/set_names.json')
        .then((res) => res.json())
        .catch((e) => console.warn(e));

    export let params;
    let search_term;
    let search_results = [];
    onMount(() => {
        search_term.addEventListener('change', () => {
            let req = new XMLHttpRequest();
            req.addEventListener('readystatechange', () => {
                if (this.readystate == 4 && this.status == 200) {
                    search_results = JSON.parse(this.responseText);
                }
            });
            req.open("GET", "/search?term=" + encodeURIComponent(search_term.value), true);
            req.send();
        });
    });
</script>


<div id="container" class="container" style="--primary: {params.get('primary')}; --secondary: {params.get('secondary')}; --background: {params.get('background')};">
    <div id="header" class="container">
        <h2><a href="https://github.com/istditajrz/practice-noun/" id="title" target="_blank" rel="noopener noreferrer">Practice-noun</a></h2>
        <span>By <i><a href="https://github.com/istditajrz" style="color: darkgrey;" target="_blank" rel="noopener noreferrer">Istditajrz</a></i></span>
    </div>
    <div class="container">
        <div class="input-group mb-3" id="box">
            <input type="text" class="form-control" placeholder="Search" aria-label="searchbar" id="searchbar" bind:this={search_term}>
            <button class="btn btn-secondary" type="button">Go!</button>
        </div>
        <ul class="list-group">
            {#each search_results as result}
                <li class="list-group-item">
                    <span>
                        <a 
                            href="/sets?sets={encodeURIComponent(Array.from([result]))}" 
                            class="list-group-item list-group-item-action">
                            {result}
                        </a>
                    </span>
                </li>
            {/each}
        </ul>
    </div>
    <ul class="list-group list-group-flush">
        {#await sets then it}
            {#each it.sets as set}
            <a href="/sets?{window.location.search.substring(1)}&sets={encodeURIComponent(JSON.stringify([set]))}" class="list-group-item list-group-item-action">{set}</a>
            {/each}
        {/await}
    </ul>
</div>
<style>
    .list-group-item-action {
        border-color: var(--secondary) !important;
    }
    #title {
        color: var(--primary);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-decoration: none;
    }
    #title:hover {
        color: var(--primary);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-decoration: underline var(--primary);
    }
    #header {
        padding-bottom: 5%;
    }
</style>
