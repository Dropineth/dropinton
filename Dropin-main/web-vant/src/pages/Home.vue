<script lang="ts" setup>
import { ref, onUnmounted } from 'vue';
import WebApp from '../WebApp'
import {
    Icon as VanIcon, Popup as VanPopup,
    showLoadingToast,Progress as VanProgress,
} from 'vant'

import { handleInviteFriend, handleCopyInviteLink } from '../utils'
// import router from '../router';
// import Collection from './CollectionPopup.vue';
import Collection from './Collection.vue';
import { TonConnectButton, useTonWallet } from "@townsquarelabs/ui-vue";
import { watchEffect } from 'vue';

// Define the interface for user data
interface UserData {
    id: number;
    first_name: string;
    last_name?: string;
    username?: string;
    language_code: string;
    is_premium?: boolean;
}

const userData = ref(null as unknown as UserData)
if (WebApp.initDataUnsafe.user) {
    userData.value = WebApp.initDataUnsafe.user as UserData
}
else {
    const testData = ref({
        id: '1234567890',
        first_name: 'kk🍅',
        last_name: 'xx',
        username: 'tester',
        language_code: 'zh - hans',
        is_premium: 'No',
    } as unknown as UserData)
    userData.value = testData.value
}

// const user = ref({ score: 0, gold: 0 })
// const today = ref({ score: 0, gold: 0 })
// const getUserInfo = () => {
//     fetch('/api/user?today=true').then((r) => r.json()).then(({ data }) => {
//         user.value = data.user
//         today.value = data.today
//     })
// }
// getUserInfo();
// const popup = ref();
// const showPopup = () => {
//     popup.value = {
//         show: true,
//         url: `/bridge.html?target=game&url=${encodeURIComponent('https://bullsback.com/?tgid=' + userData.value.id + '&nickname='+ userData.value.username)}`,
//         // url: `/bridge.html?target=game&url=${encodeURIComponent('https://game.ai24h.cn/?tgid=' + userData.value.id + '&nickname='+ userData.value.username)}`,
//         // url: 'https://bullsback.com',
//     };
//     // show loading 4 seconds
//     showLoadingToast({ duration: 4000, message: 'Loading...' })
//     window.__closeGameIframe = () => {
//         popup.value.show = false
//     }
// };
// onUnmounted(() => {
//     delete window.__closeGameIframe
// })

// const rankList = ref([] as { rownum: number, tid: number, score: number, username: string }[])
// const rankCount = ref(0)
// const getRank = () => {
//     // console.log('userData.value.id',userData.value.id)
//     fetch('/api/gameuser/rank?tgid=' + userData.value.id).then((r) => r.json()).then(({ data }) => {
//         // console.log('data.rankList',data.rankList)
//         rankList.value = data.rankList
//         rankCount.value = data.rankList.length
//         // console.log('getRank rankCount',rankCount.value)
//     })
// }
// const popupRank = ref(false);
// const showRankPopup= () => {
//     console.log('showRank')
//     popupRank.value = true;
//     getRank();
// }
// const htmlSrc = 'iframe/index.html'
// const show = ref(false);
// const showCollectionPopup= () => {
//     console.log('showCollectionPopup')
//     show.value = true;
// }

const show = ref(false);
const handleShowTip = (isShow: boolean) => {
    console.log('aaa',isShow)
    show.value = isShow
}

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
<div v-if="userData" class="Home">
    <div class="title">
        <span class="title-1">Tree Lotto</span>
        <span class="title-2">CD:8:36</span>
    </div>
    <div class="sub-title">
        <div class="progress"> 
            <span class="text">24/100</span>
            <VanProgress :percentage="50" stroke-width="8" pivot-text="" />
        </div>
        <div class="tree"> 
            <a @click="handleShowTip(true)" title="tree"  v-if="!show"></a>
            <div class="tree-tip" v-if="show" @click="handleShowTip(false)">
                <div class="tip-title">
                    <img src="./Home/icon-tree.png" alt="a tree" />
                    <span>A tree</span>
                </div>
                <span class="tip-desc">absorbs 17.9 kg of CO₂ over its lifetime.</span>
            </div>
        </div>
    </div>
    <div class="ton-provider">
            <TonConnectButton class="btn-wallet" />
        </div>
    <div class="text">
        <span class="text-title">Grand Prize : 70 TON (1)</span>
        <span class="text-desc">100% get NFT certificate (for buying saplings, grass seeds, solar power stations etc. permanent carbon offset proof for forest cover support)</span>
    </div>
    <div class="bottom">
        <div class="ton-drop">
            <a @click="" class="drop">Drop in (1 Ton)</a>
        </div>
        <div class="invite"> 
            <a @click="handleInviteFriend" title="invite"></a>
        </div>
    </div>
</div>
<div v-else class="Loading Todo">Loading ...</div>

<!-- <van-popup v-if="popup" v-model:show="popup.show" round position="bottom" :style="{ height: '100%' }" closeable
    close-icon="close" @closed="popup = null">
    <iframe  ref="iframe"  :src="htmlSrc"  style="width: 100%; height: auto; min-height: 100vh;"  frameborder="0"> </iframe>
</van-popup> -->

<!-- popup center: using CollectionPopup.vue -->
<!-- <van-popup v-model:show="show" style="background-color: transparent;overflow: hidden;" round position="center">
    <Collection @close="show=false" style="min-height: 100%;"/>
</van-popup> -->

<!-- popup bottom: using Collection.vue -->
<!-- <van-popup v-model:show="show" style="height: 85vh;" round position="bottom">
    <Collection @close="show=false" style="min-height: 100%;"/>
</van-popup> -->

<!-- <VanPopup v-if="popupRank" v-model:show="popupRank" position="center" class="popup-rank">
    <a data-href="close" class="RankPopupClose" style="top: -3vw; left: -1vw;" @click="popupRank = false"></a>
    <div class="rank-list">
        <div class="list-title"></div>
        <div class="list-content">
            <div class="list-item" v-for="(f, fi) in rankList" :key="f.tid">
                <div><span>{{ f.rownum }}</span></div>
                <div><span>{{ f.tid }}</span></div>
                <div><span>{{ f.score }}</span></div>
            </div>
            <div v-if="rankCount>50" class="tip">Only the last 50 records are displayed</div>
        </div>
    </div>
</VanPopup> -->


</template>

<style lang="less" scoped>
.Loading {
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 24px;
    height: 100%;
}

.Home {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    min-height: 100%;
    padding: 0 4vw 4vw;
    box-sizing: border-box;

    >* {
        flex: none;
    }
}

.title{
    display: flow-root;
    margin: 8vw 0px 0vw 0px;

    .title-1{
        float: left;
        font-size: 48px;
        font-weight:700;
        color: #fff;
    }
    .title-2{
        float: right;
        font-size: 20px;
        color: #fff;
        line-height: 58px;
    }
}

.sub-title{
    width: 100%;
    display: flex;
    flex-direction: row;
    
    .progress{
        width: 26%;
    }

    .progress span{
        color:#fff;
        font-weight: 700;
        font-size: 32px;
    }
    .tree{
        width: 74%;
        text-align:right;
        color:#fff;
        display: flex;
        justify-content: flex-end;
        // height: 11vw;
        // margin-bottom: 45px;

        span{
            color:#fff;
        }

        a {
            flex: none;
            background: 0 / 100% no-repeat;
        }

        a:nth-child(1) {
            width: 10vw;
            height: 10vw;
            background-image: url(./Home/tree.png);
        }
    }
    .tree-tip{
        box-sizing: border-box;
        width: 132px;
        height: 117px;
        background: rgba(255, 255, 255, 0.32);
        border: 1px solid #4FB9A5;
        backdrop-filter: blur(8.9px);
        border-radius: 28px;
        display:flex;
        flex-direction: column;
        padding: 15px;

        .tip-title{
            font-weight: 500;
            font-size: 22px;
            line-height: 27px;
            // display: flex;
            // justify-content: flex-start;
        }
        .tip-desc{
            font-weight: 500;
            font-size: 14px;
            text-align: left;
            line-height: 17px;
        }
        .tip-title img {
            width: 6vw;
            height: 6vw;
            margin-right:10px;
            // background-image: url(./Home/icon-tree.png);
        }
    }
}

.text{
    color: #FFFFFF;
    display:flex;
    flex-direction: column;
    justify-content: left;
    margin-top: auto;
    margin-bottom: 10px;

    .text-title{
        width: 318px;
        // height: 29px;
        font-weight: 700;
        font-size: 24px;
        line-height: 29px;
    }
    .text-desc{
        width: 320px;
        // height: 72px;
        font-weight: 500;
        font-size: 12px;
        line-height: 15px;
        color: #FFFFFF;
    }
}

.bottom{
    margin-top: 0;
    margin-bottom: 40px;
    display: flex;
    flex-direction: row;
    justify-content: center;

    .invite{
        text-align:right;
        color:#fff;
        display: flex;
        justify-content: flex-end;
        margin-left: 20px;

        a {
            flex: none;
            background: 0 / 100% no-repeat;
        }

        a:nth-child(1) {
            width: 15vw;
            height: 15vw;
            background-image: url(./Home/btn-invite.png);
        }
    }

    .ton-drop{
        box-sizing: border-box;
        width: 262px;
        height: 60px;
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid #326171;
        border-radius: 30px;
        // transform: matrix(-1, 0, 0, 1, 0, 0);
        text-align: center;
        
        .drop{
            width: 142px;
            height: 24px;
            font-weight: 700;
            font-size: 20px;
            line-height: 60px;
            color: #326171;
        }
    }
    
}



</style>