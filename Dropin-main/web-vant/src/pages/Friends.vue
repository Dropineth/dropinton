<script setup lang="ts">
import { ref } from 'vue';
import { Icon as VanIcon } from 'vant'
import { handleInviteFriend, handleCopyInviteLink } from '../utils'
import IconCopy from '../assets/copy-b.png'


const show = ref(false);
const friends = ref([] as { uid: string, first_name: string, username: string }[])
const goldCount = ref(0)
const scoresCount = ref(0)
const fetchData = async () => {
    const response = await fetch('/api/friends')
    const { data } = await response.json()
    goldCount.value = data.golds.reduce((p: number, c: { gold: number }) => p + c.gold, 0)
    scoresCount.value = data.scores.reduce((p: number, c: { score: number }) => p + c.score, 0)
    friends.value = data.friends

    if (friends.value.length == 0) {
        show.value = true;
    }
};
fetchData();


</script>

<template>
<div class="Friends">
    <div class="h2" title="Invite Friends" />
    <div class="cards">
        <div class="card">
            <div class="h3">Friends Number</div>
            <div class="value">X{{ friends.length }}</div>
        </div>
        <div class="card">
            <div class="h3">Incomes</div>
            <div class="value">X{{ scoresCount }}</div>
        </div>
    </div>
    <ul class="incomes">
        <li>Invite a friend <b> +100 </b> for you</li>
    </ul>
    <div class="list">
        <div class="list-title">
            <h2>List of your friends ({{ friends.length }})</h2>
        </div>
        <div class="list-0" v-show="show">
            You haven't invited anyone yet
        </div>
        <div v-for="(f, fi) in friends" :key="f.uid">
            <ul class="list-1" v-show="!show">
                <li><a href="#"><span>{{ fi + 1 }}</span>{{ f.username || f.first_name }}</a></li>
            </ul>
        </div>
        <div class="list-tip" v-show="!show">Only the last 50 records are displayed</div>
    </div>
    <div class="invite-buttons">
        <a @click="handleInviteFriend" title="Invite Friends"></a>
        <a @click="handleCopyInviteLink" title="Copy"></a>
    </div>
</div>
</template>


<style lang="less" scoped>
.Friends {
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

.h2 {
    display: block;
    height: 10vw;
    margin: 8vw 0;
    background: url(./Friends/h2.png) 50% / 51vw no-repeat;
}

.cards {
    display: flex;
    justify-content: space-between;
    padding: 0 2vw;
}

.card {
    flex: none;
    box-sizing: border-box;
    width: 42vw;
    height: 25vw;
    padding: 5vw 0 0 3vw;
    background: url(./Friends/card-bg.png) 0 / 100%;

    .h3 {
        height: 7vw;
    }

    .value {
        height: 10vw;
        padding-left: 13vw;
        line-height: 9vw;
    }
}

.card:nth-child(1) .value {
    background: url(./Friends/card-1.png) 1vw 0 / 11vw no-repeat;
}

.card:nth-child(2) .value {
    background: url(./Friends/card-2.png) 1vw 0 / 10vw no-repeat;
}

.list-title {
    font-size: 12px;
}

.list-tip {
    margin-bottom: 20px;
    font-size: 12px;
}

.list-0 {
    height: 14vw;
    line-height: 14vw;
    text-align: center;
    background: url(./Friends/items-0.png) 0 / contain no-repeat;
}

.list-1 {
    background: #1b1b1b;
    border-radius: 8px;
    margin-bottom: 20px;
    height: 50px;
    line-height: 50px;
    padding-left: 20px;
    color: #fff;
    display: flex;
    // vertical-align: middle;

    a {
        color: #fff;
        font-size: 14px;
    }

    a span {
        height: 18px;
        width: 18px;
        color: fff;
        background-color: #0052d9;
        display: inline-block;
        border-radius: 50%;
        line-height: 18px;
        text-align: center;
        margin-right: 15px;
        font-size: 12px;
    }

}

.list-friends {
    background: #1b1b1b;
    border-radius: 8px;
    margin-bottom: 20px;
}



.incomes {
    margin: 15px;
    font-size: 13px;
    list-style: disc;

    b {
        color: red;
    }

    li {
        padding: 2px 0 3px;
    }
}


.invite-buttons {

    position: fixed;
    left: 14vw;
    right: 11vw;
    bottom: 23vw;
    height: 11vw;
    display: flex;
    justify-content: space-between;

    a {
        flex: none;
        background: 0 / 100% no-repeat;
    }

    a:nth-child(1) {
        width: 63vw;
        height: 11vw;
        background-image: url(./Friends/btn-invite.png);
    }

    a:nth-child(2) {
        width: 10vw;
        height: 10vw;
        background-image: url(./Friends/btn-copy.png);
    }

}
</style>