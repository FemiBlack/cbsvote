import Vue from 'vue';
import VueRouter from 'vue-router';
import store from '@/store';

import Home from '@/views/Home.vue';
import Categories from '@/views/Categories.vue';
import CatType from '@/views/CatType.vue';
import Login from '@/views/Login.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { guest: true },
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: () => import(/* webpackChunkName: "SignUp" */ '@/views/SignUp.vue'),
    meta: { guest: true },
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import(/* webpackChunkName: "Admin" */ '@/views/Admin.vue'),
    beforeEnter: (to, from, next) => {
      console.log(store.state.auth.role);
      if (store.state.auth.role === 2) {
        next();
        return;
      }
      next('/');
    },
  },
  {
    path: '/categories',
    name: 'Categories',
    component: Categories,
  },

  {
    path: '/categories/:cat_type',
    name: 'CatType',
    component: CatType,
    props: true,
  },

  {
    path: '/404',
    alias: '*',
    name: 'notFound',
    component: () => import(/* webpackChunkName: "NotFound" */ '../views/NotFound.vue'),
  },
];

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (store.getters.isAuthenticated) {
      next();
      return;
    }
    next('/');
  } else {
    next();
  }
});
router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.guest)) {
    if (store.getters.isAuthenticated) {
      next('/');
      return;
    }
    next();
  } else {
    next();
  }
});

export default router;
