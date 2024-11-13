<template>
    <div class="default-layout">
        <aside>
            <header class="logo">
                <img src="@/assets/logo.png" alt="" :style="{height: '40%',width:'20%'}"/>
                <h2>Reports</h2>
            </header>
            <nav>
                <section class="nav-section">
                    <div class="section-title">DASHBOARDS</div>
                    <section>
                        <a href="#">
                            <span>Reporting</span>
                            <div class="subs">
                                <router-link :to="{name: 'orders'}">Orders</router-link>
                                <router-link :to="{name: 'products'}">Products</router-link>
                                <router-link :to="{name: 'suppliers'}">Suppliers</router-link>
                            </div>
                        </a>
                    </section>
                </section>
            </nav>
        </aside>
        <main class="body">
            <router-view :key="route.path"></router-view>
        </main>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useRoute } from 'vue-router';
export default defineComponent ({
    setup() {
        const route = useRoute()

        return {
            route
        }
    }
})
</script>

<style lang="">
    
</style>