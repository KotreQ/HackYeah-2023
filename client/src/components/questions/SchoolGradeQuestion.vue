<script>
let multiple = [];

export default {
    data() {
        return {
            questions: [
                { id: 0, title: 'Question 1' },
                { id: 1, title: 'Question 2' },
                {
                    id: 2,
                    title: 'Question 3',
                    answers: ['Szkola srednia', 'Szkola wyzsza'],
                    typeOfQuestion: 'single',
                },
            ],
        };
    },

    methods: {
        checkButton() {
            if (typeOfQuestion === 'multiple') {
            }
        },
    },
};

let currentQuestionId = 0;
</script>

<template>
    <div class="container">
        <div v-for="question in questions" :key="question.id">
            <h2 v-if="question.id === 0">
                {{ question.title }}
            </h2>

            <div
                class="answer"
                v-for="(answer, index) in question.answers"
                :key="index"
            >
                {{ answer }}
            </div>
        </div>

        <div
            class="anserws"
            v-for="(answer, index) in questions.answers"
            :key="index"
        >
            {{ answer }}
        </div>
    </div>
</template>
