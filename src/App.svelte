<script>
    // import SetShowcase from './SetShowcase.svelte';
	// import SentenceGroup from './SentenceGroup.svelte';
    // let set = {
    //     "subject": "they",
    //     "object": "them",
    //     "reflexive": "themselves",
    //     "possessive adjective": "their",
    //     "possessive pronoun": "theirs"
    // }
    // let name = "they/them";
	import MainPage from './MainPage.svelte';
</script>

<main>
	<MainPage/>
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
