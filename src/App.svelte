<script>
    import SetShowcase from './SetShowcase.svelte';
    let set = {
        "subject": "they",
        "object": "them",
        "reflexive": "themselves",
        "possessive adjective": "their",
        "possessive pronoun": "theirs"
    }
    let name = "they/them";
</script>

<main>
	<SetShowcase {set} {name}/>
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
