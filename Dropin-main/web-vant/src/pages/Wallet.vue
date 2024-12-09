<script setup lang="ts">
// import { ref } from 'vue';
// import { Cell as VanCell, CellGroup as VanCellGroup, Popup as VanPopup, Overlay as VanOverlay } from 'vant'

import { TonConnectButton, useTonWallet } from "@townsquarelabs/ui-vue";
import { watchEffect } from 'vue';


// const show = ref(false);
// const showPopup = () => {
//     show.value = true;
// };

const wallet = useTonWallet();
console.log('wallet account:', wallet.value?.account);
console.log('wallet account address:', wallet.value?.account.address);

const saveWallet = () => {
    fetch('/api/wallet/update', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ account: wallet.value!.account }),
    }).then((res) => res.json()).then((json) => {
        console.log('wallet saved', json)
    })
}

watchEffect(() => {
    if (wallet.value) {
        saveWallet()
    }
    return wallet.value?.account.address
})

</script>

<template>
<div class="Wallet">
    <div class="h2" title="Wallet"></div>
    <div class="h3" title="Airdrop tasks"></div>
    <div class="content">Listing is on its way.Tasks will appear below. Complete them to participate in the Airdrop
    </div>
    <div class="ton-provider">
        <div class="ton-title">Tasks List</div>
        <TonConnectButton class="btn-wallet" />
    </div>
    <!-- <div class="info" title="Coming Soon"></div> -->
</div>
</template>

<style lang="less" scoped>
.Wallet {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    min-height: 100vh;
    box-sizing: border-box;
    padding: 10vw 6vw 19vw;
    margin-bottom: 19vw;
    background: #000;
    color: #fff;

    >* {
        flex: none;
    }
}

.h2 {
    height: 41vw;
    background: url(./Wallet/h2.png) 50% / 41vw no-repeat;
}

.h3 {
    height: 10vw;
    margin: -4vw;
    background: url(./Wallet/btn-tasks.png) 50% / 61vw no-repeat;
}

.content {
    margin: 7vw 0;
    color: #fff;
}

.ton-provider {
    margin: 0 22vw;
}

.btn-wallet {
    display: block;
    width: 54vw;
    height: 12vw;
    margin: 4vw auto;
    background: url(./Wallet/btn-wallet.png) 0 / 100% no-repeat;
}

.info {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    bottom: 0;
    z-index: 10;
    background: rgba(0, 0, 0, 0.7) url(./Wallet/info.png) 50% 105vw/ 62vw no-repeat;
}
</style>