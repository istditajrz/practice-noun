<script>
    import Sentence from './Sentence.svelte';
    export let name = "they/them";
    export let sentences = ["[Their] scarf is nice"];
    let components = [];
    function check() {
        for (let i = 0; i < components.length; i++) {
            let list_element = document.getElementById("li " + i);
            if (components[i].check()) {
                list_element.className = "list-group-item list-group-item-success";
                let text = document.createElement('span');
                text.innerHTML = sentences[i].replace(/\[/g, "<strong><i>").replace(/\]/g, "</i></strong>");
                list_element.removeChild(document.getElementById("span " + i));
                list_element.appendChild(text);
            } else {
                list_element.className = "list-group-item list-group-item-danger";
            }
        }
    }
    document.addEventListener('keyup', ev => {
        if (ev.key === "Enter") {
            let next = document.getElementById((parseInt(ev.target.id) + 1));
            if (next != null) {
                next.focus();
            } else {
                check();
            }
        }
    });
</script>

<div class="container" style="margin-top: 2%;">
    <h3><i>{name}</i></h3>
    <ul class="list-group">
        <li class="list-group-item">
            <h2><i><strong>Sentences</strong></i></h2>
        </li>
        {#each sentences as sentence, index}
            <li class="list-group-item" id={"li " + index}>
                <Sentence str={sentence} id={index} bind:this={components[index]}/>
            </li>
        {/each}
        <li class="list-group-item">
            <button type="button" class="btn btn-primary" on:click={check}>Check!</button>
        </li>
    </ul>
</div>
<style>
    .container {
        width: 50%;
        background-color: darkorchid;
        border-radius: 2%;
        padding: 5%;
    }
</style>