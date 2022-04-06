<script>
    import Sentence from './Sentence.svelte';
    export let set = {
        "subject": null,
        "object": null,
        "reflexive": null,
        "possessive adjective": null,
        "possessive pronoun": null
    }; // pronoun set following the JSON format in ../assets
    export let name = null;
    export let sentences = ["[Their] scarf is nice"];
    const colors = [
        "salmon",
        "pink",
        "blue",
        "grey",
        "red",
        "orange",
        "purple",
        "navy",
        "teal",
        "antiquewhite",
        "aquamarine",
        "blanchedalmond",
        "blueviolet",
        "cadetblue",
        "chartreuse",
        "chocolate",
        "coral",
        "cornflowerblue",
        "crimson",
        "darkblue",
        "darkgray",
        "darkgreen",
        "green",
        "darkmagenta",
        "magenta",
        "darkolivegreen",
        "darkorange",
        "darkorchid",
        "orchid",
        "darkred",
        "darkseagreen",
        "darkslateblue",
        "darkslategrey",
        "darkviolet",
        "deeppink",
        "dimgrey",
        "dodgerblue",
        "firebrick",
        "floralwhite",
        "forestgreen",
        "greenyellow",
        "hotpink",
        "indianred",
        "indigo",
        "lavendar",
        "lawngreen",
        "lightblue",
        "lightcoral",
        "lightgrey",
        "lightpink",
        "lightsalmon",
        "lightseagreen",
        "lightskyblue",
        "lightslategrey",
        "lightsteelblue",
        "mediumaquamarine",
        "mediumblue",
        "mediumorchid",
        "mediumpurple",
        "mediumseagreen",
        "mediumslateblue",
        "mediumspringgreen",
        "mediumturquoise",
        "mediumvioletred",
        "midnightblue",
        "olivedrab",
        "orangered",
        "palegreen",
        "palevioletred",
        "peachpuff",
        "peru",
        "plum",
        "powderblue",
        "royalblue",
        "saddlebrown",
        "sandybrown",
        "seagreen",
        "sienna",
        "skyblue",
        "slateblue",
        "slategrey",
        "springgreen",
        "steelblue",
        "thistle",
        "violet",
        "yellowgreen",
        "rebeccapurple"
    ];
    colors.random = () => {
        return colors[Math.floor(colors.length * Math.random())];
    }
    let components = [];
    function check() {
        for (let i = 0; i < components.length; i++) {
            if (components[i].check()) {
                document.getElementById("li " + i).className = "list-group-item list-group-item-success";
            } else {
                document.getElementById("li " + i).className = "list-group-item list-group-item-danger";
            }
        }
    }
</script>

<div class="container">
    <h2 style="color: {colors.random()};">{name}</h2>
    <h3><strong><i>Forms</i></strong></h3>
    {#each Object.keys(set) as key}
        <div class="row">
            <div class="col">
                <span><strong>{key}:</strong></span>
            </div>
            <div class="col">
                <span>{set[key]}</span>
            </div>
        </div>
    {/each}
</div>
<div class="container" style="margin-top: 5%;">
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
