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

                    <section :class="{'is-toggled':toggledViews.includes('reporting')}">
                        <a href="#" @click.prevent="toggleViews('reporting')">
                            <span>Reporting</span>
                        </a>
                            <div class="subs">
                                <router-link :to="{name: 'orders'}">Orders</router-link>
                                <router-link :to="{name: 'products'}">Products</router-link>
                                <router-link :to="{name: 'suppliers'}">Suppliers</router-link>
                            </div>
                    </section>

                    <section :class="{'is-toggled':toggledViews.includes('relations')}">
                        <a href="#" @click.prevent="toggleViews('relations')">
                            <span>Relations</span>
                        </a>
                        <div class="subs">
                                <router-link :to="{name: 'customers'}">Customers</router-link>
                        </div>
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
import { defineComponent, ref } from 'vue';
import { useRoute } from 'vue-router';
import router from '@/router';
export default defineComponent ({
    setup() {
        const route = useRoute()
        
        const toggledViews = ref(
            [router.currentRoute.value.meta.screen].filter(Boolean)
        )

        const toggleViews = (key: string) => {

            if(toggledViews.value[0]===key) {
                toggledViews.value = ['']
            } else {
                toggledViews.value = [key]
            }
        }

        return {
            route,
            toggledViews,
            toggleViews
        }
    }
})
</script>

<style lang="">
    
</style>