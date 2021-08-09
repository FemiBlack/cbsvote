import axios from 'axios';
import 'sweetalert2/dist/sweetalert2.min.css';
/* eslint no-shadow: ["error", { "allow": ["state"] }] */
const state = {
  user: {
    id: '',
    email: '',
    role: ''
  },
  leads: null,
};
const getters = {
  isAuthenticated: (state) => !!state.user.id,
  StateLeads: (state) => state.leads,
  StateUser: (state) => state.user,
};
const actions = {
  async LogIn({ commit }, payload) {
    localStorage.setItem('token', payload.res.data.token);
    const role = parseInt(payload.res.data.role, 10);
    const userData = {
      'id': payload.res.data.id,
      'email': payload.User.email,
      'role': role,
    };
    await commit('setUser', userData);
  },
  async CreateNominee({ dispatch }, nominee) {
    await axios.post('/api/addnominee', nominee, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    await dispatch('GetLeads');
  },
  async UpdateNominee({ dispatch }, { payload, nomineeID }) {
    await axios.put(`/api/addnominee/${nomineeID}`, payload, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem('token')}`,
      },
    });
    await dispatch('GetUserHouses');
  },
  async GetCategory({ commit }, houseID) {
    const response = await axios.get(`/api/category/${houseID}`);
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
  setUser(state, payload) {
    state.user = payload;
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
    // state.houses = null;
  },
};

export default {
  state,
  getters,
  actions,
  mutations,
};
