<template>
    <Button class="question__button" @click="click"
        ><img src="../../assets/arrow-left.svg" alt="Poprzednie pytanie"
    /></Button>
    <Button @click="click"
        ><img src="../../assets/arrow-right.svg" alt="Nastepne pytanie"
    /></Button>
</template>

<script setup lang="ts">
import { Query } from '../query';

const props = defineProps({
    question_id: Number,
    next_question_id: Number,
    query: Query,
});

function click() {
    // Sending to server code
    props.query.current_question_id.value = props.next_question_id;
}
</script>
