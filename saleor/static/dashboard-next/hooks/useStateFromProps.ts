import { Dispatch, SetStateAction, useEffect, useState } from "react";

function useStateFromProps<TData>(
  initial: TData | (() => TData)
): [TData, Dispatch<SetStateAction<TData>>] {
  const [data, setData] = useState(initial);

  useEffect(() => setData(initial), [initial]);

  return [data, setData];
}

export default useStateFromProps;
