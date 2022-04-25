<script>
    import MainPage from './MainPage.svelte';
    export let params;
</script>

<main style={`background-color: ${params.get('background')}`}>
    <MainPage {params}/>
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
