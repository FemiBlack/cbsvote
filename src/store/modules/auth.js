import axios from 'axios';
import 'sweetalert2/dist/sweetalert2.min.css';
/* eslint no-shadow: ["error", { "allow": ["state"] }] */
const state = {
  user: null,
  role: null,
  leads: null,
};
const getters = {
  isAuthenticated: (state) => !!state.user,
  StateLeads: (state) => state.leads,
  StateUser: (state) => state.user,
  StateUserRole: (state) => state.role,
};
const actions = {
  async LogIn({ commit }, payload) {
    localStorage.setItem('token', payload.res.data.token);
    const role = parseInt(payload.res.data.role, 10);
    await commit('setUser', payload.User.email);
    await commit('setUserRole', role);
  },
  async CreateNominee({ dispatch }, nominee) {
    await axios.post('/api/addnominee', nominee, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    await dispatch('GetAllHouses');
  },
  async UpdateNominee({ dispatch }, { payload, nomineeID }) {
    await axios.put(`/api/building/${nomineeID}`, payload, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    await dispatch('GetUserHouses');
  },
  async GetCategory({ commit }, houseID) {
    const response = await axios.get(`/api/building/${houseID}`);
    commit('setHouse', response.data);
  },
  async GetLeads({ commit }) {
    const response = await axios.get('/api/building');
    commit('setAllHouses', response.data);
  },
  async DeleteNominee({ dispatch }, houseID) {
    await axios.delete(`/api/building/${houseID}`, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    await dispatch('GetUserHouses');
    // commit('SET_PRODUCTS', { products: res.data, houseID });
  },
  async LogOut({ commit }) {
    const user = null;
    commit('logout', user);
  },
};
const mutations = {
  setUser(state, username) {
    state.user = username;
  },
  setUserRole(state, role) {
    state.role = role;
  },
  setHouse(state, house) {
    state.house = house;
  },
  setAllHouses(state, houses) {
    state.houses = houses;
  },
  setDeleteNominee(state, houses) {
    state.houses = houses.id;
  },
  logout(state) {
    state.user = null;
    state.houses = null;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
