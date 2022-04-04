<script>
    const re = /\[\w+\]/g;
    export let str = "[They] smiled";
    let pronouns = [...str.matchAll(re)];
    let other = [...str.split(re)].reverse();
    let sentence = [other.pop()];
    for (let pronoun of pronouns) {
        let element = document.createElement('input');
        element.name = pronoun[0][0];
        sentence.push(element.outerHTML);
        sentence.push(other.pop());
    }
    let out = sentence.join("");
</script>

<div class="container">
    <span style="display: inline-block;">{@html out}</span>
</div>
<style>
    input {
        height: 0%;
        border-radius: 20%;
        color: antiquewhite;
        opacity: 0%;
        width: 10%;
    }
</style>