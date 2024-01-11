const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import('pages/LoginPage.vue')
  },
  {
    path: '/reset',
    component: () => import('pages/ResetPassword.vue')
  },
  {
    path: '/registration',
    component: () => import('pages/RegistrationPage.vue')
  },
  {
    path: "/",
    component: () => import('pages/MainPage.vue')
  },
  {
    path: "/categories",
    component: () => import('pages/CategoriesPage.vue')
  },
  {
    path: "/about",
    component: () => import('pages/AboutUsPage.vue')
  },
  {
    path: "/account",
    name: 'account',
    component: () => import('pages/AccountPage.vue')
  },
  {
    path: "/bucket",
    component: () => import('pages/BucketPage.vue')
  },
  {
    path: "/product",
    component: () => import('pages/ProductPage.vue')
  },
    {
    path: "/change_password",
    name: 'change_password',
    component: () => import('pages/ChangePassword.vue')
  }
]

export default routes
