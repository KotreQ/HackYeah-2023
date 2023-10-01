import { createRouter, createWebHistory } from 'vue-router';
import Quiz from '@/views/Quiz.vue';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'quiz',
            component: Quiz,
        },
    ],
});

export default router;
