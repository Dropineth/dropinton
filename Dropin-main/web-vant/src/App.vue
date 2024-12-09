<script setup lang="ts">
import { reactive, ref } from 'vue';
import { TonConnectUIProvider } from '@townsquarelabs/ui-vue';
import WebApp from './WebApp'
import router from './router';
import Home from './pages/Home.vue';
import Friends from './pages/Friends.vue';


const options = CONFIG['ton']
console.log(options)

const active = ref(0)
// const pages = [Home, Friends, Tasks, Wallet]
const pages = [Home, Friends]
const loginUser = ref(null)

// const userData = ref(null as unknown as UserData)
const login = async () => {
    const { user, start_param } = WebApp.initDataUnsafe;
    const inviterId = start_param?.slice(3)
    const request = await fetch(`/api/login${inviterId ? '?inviter=' + inviterId : ''}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user),
    })
    const body = await request.json()
    console.log('user', body)
    loginUser.value = body.data
}

// if (WebApp.initDataUnsafe.user) {
login();
// userData.value = WebApp.initDataUnsafe.user as UserData
// }
const app = ref();
const activeTab = (tab: number) => {
    active.value = tab;
    setTimeout(() => {
        app.value.$el.scrollTop = 0;
    })
}
</script>

<template>
<TonConnectUIProvider :options="options" class="app" ref="app">
    <template v-if="router == '/'">
        <component v-if="loginUser" :is="pages[active]"></component>
        <!-- <div class="tabbar">
            <a :class="{ active: active === 0 }" @click="activeTab(0);"></a>
            <a :class="{ active: active === 1 }" @click="activeTab(1);"></a>
            <a :class="{ active: active === 2 }" @click="activeTab(2);"></a>
            <a :class="{ active: active === 3 }" @click="activeTab(3);"></a>
        </div> -->
    </template>
    <Collection v-else-if="router == '/collection'" @close="router = '/'"
        style="min-height: 100vh; margin-bottom: -19vw;" />
    <!-- <AutoSignPopup v-if="autoSignPopup" :autoSign="true" :data="autoSignPopup" @closed="autoSignPopup = null" /> -->
</TonConnectUIProvider>
</template>
<style lang="less">
.van-popup {
    > i.van-popup__close-icon {
        width: 22px; height: 22px;
        background: url(./pages/Collection/close1.png) 0 0 /100% 100%;
        &::before { display: none; }
    }
}
</style>
<style lang="less" scoped>
.Todo {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 24px;
    height: 100%;
}

.app {
    height: 100vh;
    overflow: auto;
    box-sizing: border-box;
    // padding-bottom: 19vw;
    // background: #FFFEBB;
    background: url(./assets/bg.png) 50% / cover no-repeat;
}

.tabbar {
    position: fixed;
    bottom: 0;
    left: 0;
    z-index: 100;

    display: flex;
    width: 100%;
    height: 19vw;
    background: url(./assets/tabbar-bg.png) 0 0 / 100% 100%;

    >a {
        width: 25%;
        flex: none;
        background: 50% / 25vw no-repeat;
    }

    >a:nth-child(1) {
        background-image: url(./assets/tabbar1-01.png);
    }

    >a:nth-child(2) {
        background-image: url(./assets/tabbar1-02.png);
    }

    >a:nth-child(3) {
        background-image: url(./assets/tabbar1-03.png);
    }

    >a:nth-child(4) {
        background-image: url(./assets/tabbar1-04.png);
    }

    >a.active:nth-child(1) {
        background-image: url(./assets/tabbar3-01.png);
    }

    >a.active:nth-child(2) {
        background-image: url(./assets/tabbar3-02.png);
    }

    >a.active:nth-child(3) {
        background-image: url(./assets/tabbar3-03.png);
    }

    >a.active:nth-child(4) {
        background-image: url(./assets/tabbar3-04.png);
    }
}
</style>
