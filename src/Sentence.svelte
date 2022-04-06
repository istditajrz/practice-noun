<script>
    const re = /\[\w+\]/g;
    export let str = "[They] smiled";
    export let id = "";
    let pronouns = [...str.matchAll(re)];
    pronouns.forEach((v, i, a) => a[i] = v[0]);
    let other = [...str.split(re)].reverse();
    export function check() {
        for (let i = 0; i < pronouns.length; i++) {
            console.info(document.getElementById(id + i), pronouns[i].slice(1, -1), document.getElementById(id + i).value !== pronouns[i].slice(1, -1));
            if (document.getElementById(id + i).value !== pronouns[i].slice(1, -1)) {
                return false;
            }
        }
        return true;
    }
</script>

<div class="container">
    <span style="display: inline-block;">
        {other.pop()}
        {#each pronouns as pronoun, index}
            <input id={id + index}>
            {other.pop()}
        {/each}
    </span>
</div>
<style>
    input {
        height: 0%;
        background-color: antiquewhite;
        opacity: 75%;
    }
</style>