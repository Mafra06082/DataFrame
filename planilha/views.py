import io
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.messages import constants
from django.contrib import messages

def principal_view(request):
    if request.method == "POST":
        # pega *todas* as planilhas enviadas
        files = request.FILES.getlist('planilhas')
        print(f"[DEBUG] {len(files)} arquivos recebidos:", [f.name for f in files])

        # Se não vier mais de um, avisa no console e renderiza o template de novo
        if len(files) < 2:
            print("[DEBUG] Menos de 2 arquivos, adicione pelo menos mais um.")

            messages.add_message(request, constants.ERROR, 'Arquivo gerado com successo.')

            return render(request, 'index.html', {
                'erro': 'Por favor faça upload de pelo menos 2 planilhas.'
            })

        # carrega cada Excel num DataFrame
        dfs = [pd.read_excel(f, engine='openpyxl') for f in files]

        # concat horizontal
        all_cols = set()
        cleaned = []
        for df in dfs:
            
            all_cols.update(df.columns)
            cleaned.append(df)

        df_final = pd.concat(cleaned, axis=1, join='outer')

        # escreve em memória e devolve download
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df_final.to_excel(writer, index=False)
        buffer.seek(0)

        response = HttpResponse(
            buffer.read(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="resultado.xlsx"'
        messages.add_message(request, constants.SUCCESS, 'Arquivo gerado com successo.')
        return response

    return render(request, 'index.html')