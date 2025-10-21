import { useFetchAppConf } from '@/hooks/logic-hooks';
import { RefreshCcw } from 'lucide-react';
import { PropsWithChildren } from 'react';
import { RAGFlowAvatar } from './ragflow-avatar';
import { Button } from './ui/button';

type EmbedContainerProps = {
  title: string;
  avatar?: string;
  handleReset?(): void;
} & PropsWithChildren;

export function EmbedContainer({
  title,
  avatar,
  children,
  handleReset,
}: EmbedContainerProps) {
  const appConf = useFetchAppConf();

  return (
    <section className="h-[100vh] flex justify-center items-center">
      <div className=" w-[80vw] border rounded-lg">
        <div className="flex justify-between items-center border-b p-3">
          <div className="flex gap-2 items-center">
            <RAGFlowAvatar avatar={avatar} name={title} isPerson />
            <div className="text-xl text-foreground">{title}</div>
          </div>
          <div className="flex-1 flex justify-center">
            <img src="/logo.svg" alt="BYZKIDS" className="h-8 w-auto" />
          </div>
          <Button
            variant={'secondary'}
            className="text-sm text-foreground cursor-pointer"
            onClick={handleReset}
          >
            <div className="flex gap-1 items-center">
              <RefreshCcw size={14} />
              <span className="text-lg ">Reset</span>
            </div>
          </Button>
        </div>
        {children}
      </div>
    </section>
  );
}
