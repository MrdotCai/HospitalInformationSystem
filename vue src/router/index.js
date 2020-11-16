import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'login',
      component: resolve => require(['../components/login.vue'], resolve)
    },
    {
      path: '/doctorlogin',
      name: 'doctorlogin',
      component: resolve => require(['../components/doctorlogin.vue'], resolve)
    },
    {
      path: '/patientlogin',
      name: 'patientlogin',
      component: resolve => require(['../components/patientlogin.vue'], resolve)
    },
    {
      path: '/patientregister',
      name: 'patientregister',
      component: resolve => require(['../components/patientregister.vue'], resolve)
    },
    {
      path: '/patientindex/:aid',
      name: 'patientindex',
      component: resolve => require(['../components/patientindex.vue'], resolve)
    },
    {
      path: '/newform/:aid',
      name: 'newform',
      component: resolve => require(['../components/newform.vue'], resolve)
    },
    {
      path: '/formindex/:aid/:bid',
      name: 'formindex',
      component: resolve => require(['../components/formindex.vue'], resolve)
    },
    {
      path: '/doctorindex/:aid',
      name: 'doctorindex',
      component: resolve => require(['../components/doctorindex.vue'], resolve)
    },
    {
      path: '/diagnoseinfo/:aid/:bid',
      name: 'diagnoseinfo',
      component: resolve => require(['../components/diagnoseinfo.vue'], resolve)
    },
    {
      path: '*',
      name: 'error',
      component: resolve => require(['../components/404.vue'], resolve)
    }
  ]
})
