<script>
    export let set = {
        "subject": null,
        "object": null,
        "reflexive": null,
        "possessive adjective": null,
        "possessive pronoun": null
    }; // pronoun set following the JSON format in ../assets
    export let name = null;
    export let params;
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
</script>

<div class="container" style="--primary: {params.get('primary')}; --secondary: {params.get('secondary')}; --background: {params.get('background')};">
    <h2 style="color: {colors.random()};">{name}</h2>
    <h3><strong><i>Forms</i></strong></h3>
    {#each Object.keys(set) as key}
        <div class="row">
            <div class="col key">
                <span><strong>{key}:</strong></span>
            </div>
            <div class="col value">
                <span>{set[key]}</span>
            </div>
        </div>
    {/each}
</div>
<style>
    .container {
        width: 50%;
        background-color: darkorchid;
        border-radius: 2%;
        padding: 5%;
    }
    .key {
        color: var(--secondary);
    }
    .value {
        color: var(--primary);
    }
</style>
