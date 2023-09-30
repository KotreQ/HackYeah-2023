<template>
    <InputText @update:modelValue="keyInput"></InputText>
</template>

<script setup lang="ts">
import { Query } from '../query';

const props = defineProps({
    question_id: Number,
    next_question_id: Number,
    query: Query
});

function keyInput(value: String | undefined) {
    let data = props.query.getData();
    data.forEach((v, i) => {
        if (v[0] == props.question_id) {
            data.splice(i, 1);
        }
    });
    data.push([props.question_id, value]);
    console.log(data)
    props.query.setData(data);
}
</script>

<style scoped>

</style>