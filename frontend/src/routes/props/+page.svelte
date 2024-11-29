<script lang="ts">
import type { PageData } from './$types';

type PlayerData = {
    date: string;
    line: number;
    name: string;
    last10: string;
    last5: string;
    lastheadtohead: string;
    position: string;
}

type PlayerStats = {
    [key: string]: PlayerData[];
}

export let data: PageData;

const BACKEND_DATA = data.data;
const PLAYER_PROP_DATA: PlayerStats = BACKEND_DATA.playerStats;
const PLAYER_PROP_COLUMNS = ["Date", "Line", "Name", "Last5", "Last10", "Head to Head", "Over/Under"]

let selectedDate = Object.keys(PLAYER_PROP_DATA)[Object.keys(PLAYER_PROP_DATA).length - 1];
</script>

<select name="date" id="prop_date" bind:value={selectedDate} class="mb-4 p-2 border rounded">
    {#each Object.keys(PLAYER_PROP_DATA) as date}
        <option value={date}>{date}</option>
    {/each}
</select>
<table class="w-full table-auto border-collapse">
    <thead>
        <tr class="bg-gray-100">
            {#each PLAYER_PROP_COLUMNS as column}
                <td class="p-3 text-left font-semibold">{column}</td>
            {/each}
        </tr>
    </thead>
    <tbody>
        {#if PLAYER_PROP_DATA[selectedDate]?.length === 0}
            <tr>
                <td colspan={PLAYER_PROP_COLUMNS.length} class="text-center p-4">No data available</td>
            </tr>
        {:else}
            {#each PLAYER_PROP_DATA[selectedDate] as player_data, i}
                <tr>
                    <td class="p-3">{player_data["date"]}</td>
                    <td class="p-3">{player_data["name"]}</td>
                    <td class="p-3">{player_data["line"]}</td>
                    <td class="p-3">{player_data["last5"]}</td>
                    <td class="p-3">{player_data["last10"]}</td>
                    <td class="p-3">{player_data["lastheadtohead"]}</td>
                    <td class="p-3">
                        {player_data["position"]}
                        <span>
                            {#if player_data["position"] == "over"}
                            &uarr;
                            {:else}
                            &darr;
                            {/if}
                        </span>
                    </td>
                </tr>
            {/each}
        {/if}
    </tbody>
</table>