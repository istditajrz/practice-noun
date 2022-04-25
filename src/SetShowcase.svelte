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
    <div class="row gutter">
        <div class="col key">
            <span><strong><i>Subject:</i></strong></span>
        </div>
        <div class="col value">
            <span>{set.subject}</span>
        </div>
    </div>
    <div class="row gutter">
        <div class="col key">
            <span><strong><i>Object:</i></strong></span>
        </div>
        <div class="col value">
            <span>{set.object}</span>
        </div>
    </div>
    <div class="row gutter">
        <div class="col key">
            <span><strong><i>Reflexive:</i></strong></span>
        </div>
        <div class="col value">
            <span>{set.reflexive}</span>
        </div>
    </div>
    <div class="row gutter">
        <div class="col key">
            <span><strong><i>Possessive Adjective:</i></strong></span>
        </div>
        <div class="col value">
            <span>{set["possessive adjective"]}</span>
        </div>
    </div>
    <div class="row">
        <div class="col key">
            <span><strong><i>Possessive Pronoun:</i></strong></span>
        </div>
        <div class="col value">
            <span>{set["possessive pronoun"]}</span>
        </div>
    </div>
</div>
<style>
    .container {
        width: 50%;
        background-color: var(--primary);
        border-radius: 2%;
        padding: 5%;
        margin-bottom: 2%;
    }

    h2 {
        text-align: center;
    }

    h3 {
        text-align: center;
    }
    
    .gutter {
        border-bottom: 1px solid var(--secondary);
    }

    .col {
        color: var(--secondary);
    }
</style>
