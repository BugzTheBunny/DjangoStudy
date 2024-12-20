import { createRouter, createWebHashHistory, RouteRecordRaw } from 'vue-router'
import OrdersView from '@/views/reporting/screens/OrdersView.vue'
import ProductView from '@/views/reporting/screens/ProductView.vue'
import SupplierView from '@/views/reporting/screens/SupplierView.vue'
import DashboardView from '@/views/DashboardView.vue'
import CustomersView from '@/views/relations/screens/CustomersView.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'dashboard',
    component: DashboardView,

    children: [
      {
        path: '/orders',
        name: 'orders',
        component: OrdersView,
        meta: {screen: "orders"},

      },
      {
        path: '/products',
        name: 'products',
        component: ProductView,
        meta: {screen: "products"},

      },
      {
        path: '/suppliers',
        name: 'suppliers',
        component: SupplierView,
        meta: {screen: "suppliers"},

      },
      {
        path: '/customers',
        name: 'customers',
        component: CustomersView,
        meta: {screen: "customers"},
      }
    ]
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
