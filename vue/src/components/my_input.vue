<template>
  <h2>{{ head }}</h2>

  <div>
    <el-input v-loading="loading"
              v-model="input_text"
              style="width: 25vw;height: 35vh;"
              :autosize="{ minRows: 10, maxRows: 10 }"
              type="textarea"
              placeholder="Please input"
    />
  </div>

  <el-button type="success" size="large" plain @click="submit()">
    生成知识图谱
  </el-button>

  <div v-show="show" class="result">
    <div>
      <h3>nodes</h3>
      <div>
        <el-input
            v-model="nodes"
            style="width: 25vw;height: 35vh;"
            :autosize="{ minRows: 10, maxRows: 10 }"
            type="textarea"
        />
      </div>
    </div>
    <div>
      <h3>links</h3>
      <div>
        <el-input
            v-model="links"
            style="width: 25vw;height: 35vh;"
            :autosize="{ minRows: 10, maxRows: 10 }"
            type="textarea"
        />
      </div>
    </div>
  </div>

</template>

<script lang="ts" setup>
import {ref} from 'vue'

const head = ref('请输入原始本文')
const input_text = ref('')
import {create_knowledge_graph} from '../api/api.js'

const loading = ref(false)
const show = ref(false)
const nodes = ref('')
const links = ref('')

function submit() {
  head.value = '等待响应中... 实体抽取和关系抽取速度很慢。'
  loading.value = true
  const data = {text: input_text.value}
  create_knowledge_graph(data).then(response => {
    loading.value = false
    show.value = true
    console.log(response.data)
    console.log(JSON.stringify(response.data))
    const arr = format(response.data)
    nodes.value = JSON.stringify(arr[0])
    links.value = JSON.stringify(arr[1])
  })
}


function format(triples) {

  const entities = {}
  const links = []

  for (let triple_index = 0; triple_index < triples.length; triple_index++) {
    const triple = triples[triple_index]

    // 从triple中提取实体
    const triple_entities = []
    for (const old_entity_name in triple['entities']) {
      const old_entity_type = triple['entities'][old_entity_name]
      triple_entities.push({
        'name': old_entity_name,
        'type': old_entity_type,
      })
    }

    //插入entity，记录entity索引，查重
    let entity_indexs = []
    for (const triple_entity of triple_entities) {
      let repeat = false
      for (const entity_index in entities) {
        const entity = entities[entity_index]
        console.log(entity)
        if (triple_entity['name'] == entity['name']) {
          entity['type'] = triple_entity['type']
          entity_indexs.push(entity_index)
          repeat = true
          break
        }
      }
      if (!repeat) {
        entity_indexs.push(Object.keys(entities).length)
        entities[Object.keys(entities).length] = triple_entity
      }
    }

    if (entity_indexs.length == 2) {
      links.push({
        'source': entity_indexs[0],
        'target': entity_indexs[1],
        'rela': triple['relation']
      })
    }

  }
  console.log(entities)
  console.log(links)
  return [entities, links]
}

</script>

<style>

.result {
  display: flex;
}
</style>