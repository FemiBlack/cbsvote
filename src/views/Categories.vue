<template>
    <div class="limiter">
		<section class="login-container">
			<div class="side-overlay --sm" :style="`background-image: url(${require('@/assets/images/bg.png')});width: calc(100% - 900px);`">
                <figure>
                    <img src="./images/Saly-37.svg" style="position: absolute;bottom: 0;left: 0;animation-duration: 0;" alt="ball_point">
                </figure>
			</div>
            <!-- <header>
                <h3>Categories</h3>
            </header> -->
            <div class="wrap-login" v-for="(category,i) in categories" :key="i">
                <router-link to="`/categories/{{cat.pop}}`" class="cat-border">
                    <div class="cat-name">{{ category }}</div>
                </router-link>
            </div>
        </section>
    </div>
</template>
<script>
const categories = [
    'Most Fashionable(male)',
    'Most Fashionable(female)',
    'CBS Next Gen(male)',
    'CBS Next Gen(female)',
    'Entrepreneur of the year(male)',
    'Entrepreneur of the year(female)',
    'Face of CBS(male)',
    'Face of CBS(female)',
    'Most Sociable(male)',
    'Most Sociable(female)',
    'Sportsperson of the year(male)',
    'Sportsperson of the year(female)',
    'Most Innovative(male)',
    'Most Innovative(female)',
]
export default {
    name: 'Categories',
    data() {
        return {
            categories
        }
    }
}
</script>
<style>
    .limiter {
        overflow-y: auto;
        grid-template-rows: auto;
    }
    .cat-border {
        border: 1.5px solid #2604F6;
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 26px;
    }
    .cat-name {
        font-family: Montserrat, sans-serif;
        font-weight: bold;
        /* font-size: 20px; */
        line-height: 36px;
        /* or 40% */

        text-align: center;

    }
    footer {
        position: absolute;
        bottom: 0;
        right: 9em;
    }
    header {
        background-image: url('./images/doodle.png');
        background-repeat: no-repeat;
    }
    header h3 {
        font-family: Montserrat, sans-serif;
        font-weight: bold;
        font-size: 42px;
        line-height: 32px;
        transform-style: preserve-3d;
    }
    header h3::after{
        content: '';
        position: absolute;
        width: 294px;
        height: 10px;
        left: -10px;
        top: 19px;
        transform: translateZ(-1px);

        background: linear-gradient(90deg, #4DFD5F 0%, rgba(4, 79, 226, 0.44) 100%);
        border-radius: 30px;
    }
</style>