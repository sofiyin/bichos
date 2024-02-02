import HomeView from "./components/homeView.vue";
import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "homeView",
    component: HomeView,
  },
  {
    path: "/ImageUploader",
    name: "ImageUploader",
    component: () =>
      import(/* webpackChunkName: "about" */ "./components/ImageUploader.vue"),
  },
  {
    path: "/SendSyntomas",
    name: "SendSyntomas",
    component: () =>
      import(/* webpackChunkName: "about" */ "./components/SendSyntomas.vue"),
  },

  {
    path: "/LocacionCliente",
    name: "LocacionCliente",
    meta: {
      requiresAuth: true,
    },
    component: () =>
      import(/* webpackChunkName: "about" */ "./components/LocacionCliente.vue"),
  },
  {
    path: "/ResultadosCliente",
    name: "ResultadosCliente",
    component: () =>
      import(/* webpackChunkName: "about" */ "./components/ResultadosCliente.vue"),
  }

];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
  });


export default router;