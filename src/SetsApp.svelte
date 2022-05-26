<script>
    import SetShowcase from "./SetShowcase.svelte";
    import SentenceGroup from "./SentenceGroup.svelte";
    export let params;
    console.log(decodeURIComponent(params.get('sets')));
    let sets_array = JSON.parse(decodeURIComponent(params.get('sets')));
    let sets = {};
    sets = Promise.all(
        sets_array.map(key => {
            return fetch(`/data/${key}.json`)
                .then( 
                    (v) => {
                        return v.json();
                    },
                    () => new Promise.resolve(null)
                )
                .then( (value) => { return {key: key, value: value}; } ) 
            }
        )
    )
    // let sentences = Promise.resolve({});
    // if (!params.has('sentences') || decodeURIComponent(params.get('sentences')) == true) {
    //     sentences = Promise.all(
    //         sets_array.map(key => {
    //             return fetch(`/data/sentences/${encodeURIComponent(key)}.json`)
    //                 .then(
    //                     (v) => v.json(),
    //                     ()  => new Promise.resolve(null)
    //                 )
    //                 .then( (value) => { return {key: key, value: value.sentences}; } )
    //             }
    //         )
    //     );
    // }
</script>

<main>
    {#await sets then it}
        {#each it as {key: name, value: set}}
            {#if set !== null}
                <SetShowcase {set} {name} {params}/>
            {/if}
        {/each}
    {/await}
    <!-- {#await sentences then it}
        {#each it as {key: name, value: sentenceSet}}
            <SentenceGroup sentences={sentenceSet} {name} {params}/>
        {/each}
    {/await} -->
</main>
<style>
    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;
    }
    
    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }

</style>
