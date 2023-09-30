<template>
    <Button label="Wyślij"></Button>
</template>

<script setup lang="ts">
import { Query } from '../query';

const props = defineProps({
    question_id: Number,
    query: Query
});

function click() {
    // Sending to server code
}
</script>

<style scoped>

</style>