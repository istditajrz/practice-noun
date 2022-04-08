<script>
    export let sets = [
        "he/him", "she/her", "they/them"
    ];
    let search_term;
    let search_results = [];
    document.addEventListener('DOMContentLoaded', () => {
        search_term.addEventListener('change', ev => {
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
<div id="container" class="container">
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
                            href="/sets?={encodeURIComponent(Array.from([result]))}" 
                            class="list-group-item list-group-item-action">
                            {result}
                        </a>
                    </span>
                </li>
            {/each}
        </ul>
    </div>
    <ul class="list-group list-group-flush">
        {#each sets as set}
        <a href="/sets?={encodeURIComponent(Array.from([set]))}" class="list-group-item list-group-item-action">{set}</a>
        {/each}
    </ul>
</div>
<style>
    #title {
        color: black;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-decoration: none;
    }
    #title:hover {
        color: black;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-decoration: underline black;
    }
    #header {
        padding-bottom: 5%;
    }
</style>